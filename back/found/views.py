from .models import FoundPosting, FoundThumbnail, FoundImage
from .serializers import FoundPostingSerializer, FoundImageSerializer, \
    FoundPostingDetailSerializer, CreateFoundPostingSerializer, FoundThumbnailSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from datetime import timedelta, datetime
import json
from lost.serializers import LostThumbnailSerializer, LostImageSerializer
from lost.models import LostPosting, LostThumbnail
from ai.views import get_numpy_path, get_category, get_similar_image, get_closer_user
from django.contrib.auth import get_user_model
User = get_user_model()


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

                postings = FoundPosting.objects.filter(created__gt=datetime.now() - timedelta(weeks=2))
                image_set = FoundThumbnail.objects.filter(posting_id__in=postings).values('origin')
                origin_images = FoundImage.objects.filter(id__in=image_set)
                # TODO 확인 3
                images_id_result = get_similar_image(lost_image.image, origin_images)

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
                thumbnail_image = th_serializer.create(th_serializer.validated_data)
                thumbnail_image.origin_id = image.id
                thumbnail_image.save()

                numpy_path = get_numpy_path(image)
                image.numpy_path = numpy_path
                # TODO 확인 4
                c1, c2, c3 = get_category(request.FILES['image'])
                image.category_1, image.category_2, image.category_3 = c1, c2, c3
                image.save()

                datasets = {
                    'image_id': thumbnail_image.id,
                    'category': c1,
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
            # TODO 확인 5 + 가벙 할일 여기부터 셀렉팅 시작할 것
            lost_postings = LostPosting.objects.filter(category=posting.category, color=posting.color)

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

