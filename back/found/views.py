from django.shortcuts import get_object_or_404
from .models import FoundPosting, FoundThumbnail, FoundImage
from .serializers import FoundPostingSerializer, FoundImageSerializer, \
    FoundPostingDetailSerializer, CreateFoundPostingSerializer, FoundThumbnailSerializer
from lost.serializers import LostThumbnailSerializer, LostImageSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
import json
from decouple import config
import requests
from django.views.decorators.cache import cache_page
from datetime import timedelta
from datetime import datetime
from django.contrib.auth import get_user_model
User = get_user_model()

# search_by_image 관련 module
import mahotas as mh
import numpy as np
from scipy.spatial import distance
from sklearn.model_selection import cross_validate, LeaveOneOut, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from django.conf import settings
import os
from .apps import FoundConfig


def get_closer_user(x, y, radius):
    keywords = f'x={x}&y={y}&radius={radius}&categoru_group_code=PO3&query=경찰서'
    URL = 'https://dapi.kakao.com/v2/local/search/keyword.json?&sort=distance&'
    headers = {"Authorization": f"KakaoAK {config('KAKAOAK')}"}

    url = URL + keywords
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)

    flag = False
    users = []

    if result.get('meta'):
        for item in result['documents']:
            if User.objects.filter(phone_number=item['phone']).exists():
                users.append(get_object_or_404(User, phone_number=item['phone']).id)

    else:
        flag = True

    return flag, users


@api_view(['GET'])
@permission_classes([AllowAny])
def search_found(request):
    color = request.query_params.get('color')
    category = request.query_params.get('category')
    created = request.query_params.get('created')
    x = request.query_params.get('x')
    y = request.query_params.get('y')
    radius = request.query_params.get('radius')

    posting_set = FoundPosting.objects.all()

    if category:
        posting_set = posting_set.filter(category=category)

    if x:
        radius = radius if radius else 1000
        flag, user_list = get_closer_user(x, y, radius)
        if flag:
            datasets = {'message': '유효하지 않은 요청입니다.'}
            data = json.dumps(datasets, ensure_ascii=False)
            return Response(status=403, data=data, content_type='application.json')
        if not user_list:
            return Response(status=204, content_type='application.json')
        else:
            posting_set = posting_set.filter(user_id__in=user_list)

    if created:
        posting_set = posting_set.filter(created__gte=created)

    if color:
        posting_set = posting_set.filter(color=color)

    posting_set = posting_set[:50]
    serializer = FoundPostingDetailSerializer(posting_set, many=True)

    datasets = {
        'meta': {
            'total_cnt': posting_set.count()
        },
        'documents': serializer.data
    }

    return Response(status=200, data=datasets, content_type='application.json')


@api_view(['POST'])
@permission_classes([AllowAny])
def search_by_image(request):
    if request.FILES:
        serializer = LostImageSerializer(request.POST, request.FILES)
        if serializer.is_valid():
            th_serializer = LostThumbnailSerializer(request.POST, request.FILES)
            if th_serializer.is_valid():
                lost_image = serializer.create(serializer.validated_data)
                lost_thumbnail_image = th_serializer.create(th_serializer.validated_data)
                lost_thumbnail_image.origin_id = lost_image.id
                lost_thumbnail_image.save()

                # 분실자가 Post 한 이미지 전처리 <class 'numpy.ndarray'>
                im = mh.imread(lost_image.image)
                im = mh.colors.rgb2gray(im, dtype=np.uint8)
                im_ftr = mh.features.haralick(im).ravel()

                # 3주 postings 불러오기
                postings = FoundPosting.objects.filter(created__gt=datetime.now() - timedelta(weeks=2))
                print(postings)
                image_set = FoundThumbnail.objects.filter(posting_id__in=postings).values('origin')
                print(image_set) # 해당 이미지 id 담긴 list
                origin_images = FoundImage.objects.filter(id__in=image_set)
                print(origin_images)

                # npy file 불러오기
                origin_ids = []
                origin_image_features = []
                for origin_image in origin_images:
                    real_numpy_path = os.path.join(settings.MEDIA_ROOT, origin_image.numpy_path)
                    print(real_numpy_path)
                    origin_image_feature = np.load(real_numpy_path)
                    origin_ids.append(origin_image.id)
                    print(origin_image_feature)
                    origin_image_features.append(origin_image_feature)

                origin_ids = [0] + origin_ids
                origin_image_features = [im_ftr] + origin_image_features

                origin_image_features = np.array(origin_image_features)
                # print(origin_image_features.shape)


                # features & labels numpy.array
                clf = Pipeline([('preproc', StandardScaler()),
                                ('classifier', LogisticRegression())])

                cv = LeaveOneOut()

                # scores = cross_val_score(clf, features, labels, cv=cv)
                # print('Accuracy: {:.2%}'.format(scores.mean()))

                sc = StandardScaler()
                features = sc.fit_transform(origin_image_features)

                # dists matrix 구하기 (사진 개수 X 사진 개수)
                dists = distance.squareform(distance.pdist(features, "cosine"))
                # print(*dists, sep='\n')
                # print(dists[0])
                # print(dists[0].argsort().tolist())
                similar_order = dists[0].argsort().tolist()
                first = similar_order.index(1)
                second = similar_order.index(2)
                third = similar_order.index(3)

                # return
                images_id_result = [int(first), int(second), int(third)]
                thumb_set = FoundThumbnail.objects.filter(origin_id__in=images_id_result).values('posting')
                posting_set = FoundPosting.objects.filter(id__in=thumb_set)

                serializer = FoundPostingDetailSerializer(posting_set, many=True)

                datasets = {
                    'meta': {
                        'total': posting_set.count()
                    },
                    'documents': serializer.data
                }

                return Response(status=200, data=datasets, content_type='application.json')
        return Response(status=400, data={'message': 'Invalid images input'})
    return Response(status=403, data={'message': '이미지는 필수값입니다.'})


@api_view(['POST'])
@permission_classes([AllowAny])
def create_found_image(request):
    if request.FILES:
        serializer = FoundImageSerializer(request.POST, request.FILES)
        if serializer.is_valid():
            th_serializer = FoundThumbnailSerializer(request.POST, request.FILES)
            if th_serializer.is_valid():
                image = serializer.create(serializer.validated_data)

                # FoundImage의 numpy_path 칼럼 값 저장
                im = mh.imread(image.image)
                im = mh.colors.rgb2gray(im, dtype=np.uint8)
                im_ftr = mh.features.haralick(im).ravel()
                numpy_path = str(image.image).split('.')[0] + '.npy'
                image.numpy_path = numpy_path
                image.save()
                # image 와 같은 경로 내에 [FoundImage와 같은 이름].npy 파일도 저장
                numpy_path = os.path.join(settings.MEDIA_ROOT, numpy_path)
                np.save(numpy_path, im_ftr)

                # thumbnail
                thumbnail_image = th_serializer.create(th_serializer.validated_data)
                thumbnail_image.origin_id = image.id
                thumbnail_image.save()

                # apps.py 에서 사용할 model 로드
                loaded_model = FoundConfig.model

                #TODO load keras model
                print(loaded_model) # <tensorflow.python.keras.engine.sequential.Sequential object at 0x000001A968DB56C8>
                
                #TODO predict (image input & output --> category_1, 2, 3)

                #TODO Category 분석기 결과값(추후 수정)
                category_1 = 1
                category_2 = 2
                category_3 = 3
                image.category_1 = category_1
                image.category_2 = category_2
                image.category_3 = category_3
                image.save()
                #TODO Category image 에 추가 등록하기
                datasets = {
                    'image_id': thumbnail_image.id,
                    'category': category_1,
                }
                return Response(status=200, data=datasets, content_type='application.json')
        return Response(status=400, data={'message': 'Invalid images input'})
    return Response(status=403, data={'message': '이미지는 필수 값입니다.'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_found(request):
    data = request.data
    serializer = CreateFoundPostingSerializer(data=data)
    if serializer.is_valid():
        posting = serializer.save(user=request.user, status=False)

        if data.get('image_id'):
            thumbnail = get_object_or_404(FoundThumbnail, id=data['image_id'])
            thumbnail.posting_id = posting.id
            thumbnail.save()

        posting_serializer = FoundPostingDetailSerializer(posting)
        return Response(status=200, data=posting_serializer.data)
    return Response(status=400, data={'message': 'Invalid input'})


@cache_page(60 * 2)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_found_list(request):
    postings = FoundPosting.objects.filter(user=request.user)

    serializer = FoundPostingSerializer(postings, many=True)
    datasets = {
        'meta': {
            'total': postings.count()
        },
        'documents': serializer.data
    }

    return Response(status=200, data=datasets)


@cache_page(60 * 2)
@api_view(['GET'])
@permission_classes([AllowAny])
def get_found_detail(request, found_id):
    posting = get_object_or_404(FoundPosting, id=found_id)
    serializer = FoundPostingDetailSerializer(posting)

    return Response(status=200, data=serializer.data)


@api_view(['PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def update_delete_found(request, found_id):
    posting = get_object_or_404(FoundPosting, id=found_id)
    data = request.data
    if posting.user_id == request.user.id:
        if request.method == 'PATCH':
            serializer = CreateFoundPostingSerializer(instance=posting, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=200, data=serializer.data)
            return Response(status=400, data={'message': 'Invalid input'})
        elif request.method == 'DELETE':
            posting.delete()
            return Response(status=204)
    else:
        return Response(status=400, data={'message': '권한이 없습니다.'})


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_found_status(request, found_id):
    posting = get_object_or_404(FoundPosting, id=found_id)
    if posting.user_id == request.user.id:
        posting.status = False if posting.status else True
        posting.save()
        return Response(status=204)
    else:
        return Response(status=400, data={'message': '권한이 없습니다.'})

