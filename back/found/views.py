from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .models import FoundPosting, FoundThumbnail
from .serializers import FoundPostingSerializer, FoundImageSerializer, FoundPostingListSerializer, \
    FoundPostingDetailSerializer, CreateFoundPostingSerializer, FoundThumbnailSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
import json
from decouple import config
import requests
from django.views.decorators.cache import cache_page

from django.contrib.auth import get_user_model
User = get_user_model()


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


# @cache_page(60 * 2)
@api_view(['GET'])
@permission_classes([AllowAny])
def search_found(request):
    """
    습득물 조회 + 분류

    :param category_id:
    :param request: color, category, created_at, x, y, radius
    """
    # TODO 길이 조정하기, 잘라보내기

    color = request.query_params.get('color')
    category = request.query_params.get('category')
    created = request.query_params.get('created')
    x = request.query_params.get('x')
    y = request.query_params.get('y')
    radius = request.query_params.get('radius')

    if not category:
        return Response(status=400, data={'message: category 는 필수 값입니다.'})

    posting_set = FoundPosting.objects.filter(category=category)

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

    paginator = Paginator(posting_set, 8)
    page_number = request.query_params.get('page')
    page_obj = paginator.get_page(page_number)

    serializer = FoundPostingListSerializer(page_obj, many=True)

    datasets = {
        'meta': {
            'total_cnt': paginator.count,
            'last_page': paginator.num_pages,
            'page': page_number if page_number else 1,
        },
        'documents': serializer.data
    }

    return Response(status=200, data=datasets, content_type='application.json')


@api_view(['POST'])
@permission_classes([AllowAny])
def search_by_image(request):
    """
    습득물 이미지 검색
    :param request: FILES 'image'
    :return: 최근 3주 습득물 중 유사도가 높은 게시글 최대 3개
    """
    if request.FILES:
        serializer = FoundImageSerializer(request.POST, request.FILES)
        if serializer.is_valid():
            th_serializer = FoundThumbnailSerializer(request.POST, request.FILES)
            if th_serializer.is_valid():
                image = serializer.create(serializer.validated_data)
                thumbnail_image = th_serializer.create(th_serializer.validated_data)
                thumbnail_image.origin_id = image.id
                thumbnail_image.save()

                #TODO AI 웅앵

                images_id_result = [1, 2, 3]
                posting_set = FoundPosting.objects.filter(image_id__in=images_id_result)

                serializer = FoundPostingListSerializer(posting_set, many=True)

                datasets = {
                    'meta': {
                        'image_id': thumbnail_image.id,
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
    """
    습득물 게시글 작성을 위해 이미지 제출 (header jwt 필요)

    :param request: FILES 'image'
    :return: {image_id: int, category: int, color: int}
    """
    if request.FILES:
        serializer = FoundImageSerializer(request.POST, request.FILES)
        if serializer.is_valid():
            th_serializer = FoundThumbnailSerializer(request.POST, request.FILES)
            if th_serializer.is_valid():
                image = serializer.create(serializer.validated_data)
                thumbnail_image = th_serializer.create(th_serializer.validated_data)
                thumbnail_image.origin_id = image.id
                thumbnail_image.save()

                #TODO Category 분석기
                category = 1
                #TODO Color 분석기
                color = 2
                #TODO Category image 에 추가 등록하기
                datasets = {
                    'image_id': thumbnail_image.id,
                    'category': category,
                    'color': color
                }
                return Response(status=200, data=datasets, content_type='application.json')
        return Response(status=400, data={'message': 'Invalid images input'})
    return Response(status=403, data={'message': '이미지는 필수 값입니다.'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_found(request):
    data = {
        'image_id': 3,
        'color': 3,
        'category': 2,
        'content': 'werewr'
    }

    serializer = CreateFoundPostingSerializer(data=data)
    if serializer.is_valid():
        posting = serializer.save(user=request.user, status=False)

        if data["image_id"]:
            thumbnail = get_object_or_404(FoundThumbnail, id=data["image_id"])
            thumbnail.posting_id = posting.id
            thumbnail.save()

        return Response(status=200, data=serializer.data)
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

    if posting.id == request.user:
        data = {
            'color': 6,
            'category': 2,
            'content': 'werewr'
        }
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
    if posting.id == request.user:
        posting.status = False if posting.status else True
        posting.save()
        return Response(status=204)
    else:
        return Response(status=400, data={'message': '권한이 없습니다.'})

