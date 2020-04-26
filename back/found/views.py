from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from django.core.paginator import Paginator
from .forms import FoundImageForm
from .models import FoundPosting, FoundImage, FoundThumbnail
from .serializers import FoundPostingSerializer, FoundImageSerializer,\
    FoundPostingDetailSerializer, CreateFoundPostingSerializer, CreateFoundThumbnailSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
import json
from django.core.cache import cache
from decouple import config
import requests
from .sample import CachedPaginator
from rest_framework import viewsets, permissions
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
            if User.objects.filter(center_name=item['place_name'][:-3]).exists():
                users.append(User.objects.get(center_name=item['place_name'][:-3]).id)

    else:
        flag = True

    return flag, users


@cache_page(60 * 1)
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
    created_at = request.query_params.get('createdAt')
    x = request.query_params.get('x')
    y = request.query_params.get('y')
    radius = request.query_params.get('radius')

    posting_set = FoundPosting.objects.filter(category=category)

    if x:
        radius = radius if radius else 1000
        flag, user_list = get_closer_user(x, y, radius)
        if flag:
            datasets = {'message': '유효하지 않은 요청입니다.'}
            data = json.dumps(datasets, ensure_ascii=False)
            return Response(status=400, data=data, content_type='application.json')
        if not user_list:
            return Response(status=204, content_type='application.json')
        else:
            posting_set = posting_set.filter(user_id__in=user_list)

    if created_at:
        posting_set = posting_set.filter(created_at__gte=created_at)

    if color:
        posting_set = posting_set.filter(color=color)

    paginator = Paginator(posting_set, 8)
    page_number = request.query_params.get('page')
    page_obj = paginator.get_page(page_number)

    datasets = {
        'meta': {
            'total_cnt': paginator.count,
            'last_page': paginator.num_pages,
            'page': page_number if page_number else 1,
        },
        'documents': []
    }

    for posting in page_obj.object_list:
        user = posting.user.center_name + posting.user.role

        if posting.image:
            img_path = 'media/' + str(get_object_or_404(FoundThumbnail, posting=posting.id).image)
        else:
            img_path = 'media/no_img.png'

        datasets['documents'].append({
            'id': posting.id,
            'color': posting.color.color,
            'category': posting.category.category,
            'content': posting.content,
            'status': posting.status,
            'user': user,
            'img_path': img_path
        })

    data = json.dumps(datasets, ensure_ascii=False)
    return Response(status=200, data=data, content_type='application.json')


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
            image = serializer.save()

            #TODO AI 웅앵

            images_id_result = [1, 2, 3]
            posting_set = FoundPosting.objects.filter(image_id__in=images_id_result)

            datasets = {
                'meta': {
                    'image_id': image.id,
                    'total': 0
                },
                'documents': []
            }

            for posting in posting_set:
                user = posting.user.center_name + posting.user.role
                img_path = 'media/' + str(get_object_or_404(FoundThumbnail, posting=posting.id).image)

                datasets['meta']['total'] += 1
                datasets['documents'].append({
                    'id': posting.id,
                    'color': posting.color.color,
                    'category': posting.category.category,
                    'content': posting.content,
                    'status': posting.status,
                    'user': user,
                    'img_path': img_path
                })

            data = json.dumps(datasets, ensure_ascii=False)
            return Response(status=200, data=data, content_type='application.json')
        print(serializer.errors)
        return Response(status=400, data={'Invalid images input'})
    return Response(status=400, data={'이미지는 필수값입니다.'})


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
            th_serializer = CreateFoundThumbnailSerializer(request.POST, request.FILES)
            if th_serializer.is_valid():
                serializer.create(serializer.validated_data)
                thumbnail_image = th_serializer.create(th_serializer.validated_data)

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
            return Response(status=400, data=th_serializer.errors)
        return Response(status=400, data=serializer.errors)
    return Response(status=404, data={'message': '이미지는 필수 값입니다.'})


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
            posting.image_id = data["image_id"]
            posting.save()
            thumbnail = get_object_or_404(FoundThumbnail, id=data["image_id"])
            thumbnail.posting_id = posting.id
            thumbnail.save()

        return Response(status=200, data=serializer.data)
    return Response(status=400, data=serializer.errors)



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
    if request.method == 'PATCH':
        pass
    else:
        pass


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_found_status(request, found_id):
    pass


