from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from rest_framework import generics

from .models import FoundPosting, FoundImage
from .serializers import FoundPostingSerializer, FoundImageSerializer, LazyEncoder
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import json
from django.core.cache import cache
from decouple import config
import requests
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

            # if len(users) > 4:  #TODO 아무리 반경을 크게 해도 max 있음
            #     break
    else:
        flag = True

    return flag, users


@api_view(['GET'])
@permission_classes([AllowAny])
def posting_list(request):
    """
    습득물 조회 + 분류

    query param 으로 color, category, created_at, x, y, radius 값
    [{id, color, category, content, status, user, img_path}]
    todo1. 데이터 양 많으면 잘라보내기
    todo2. cache 적용하기
    """

    color = request.query_params.get('color')
    category = request.query_params.get('category')
    created_at = request.query_params.get('createdAt')
    x = request.query_params.get('x')
    y = request.query_params.get('y')
    radius = request.query_params.get('radius')

    posting_set = FoundPosting.objects.all()  #TODO 맨 첨에 반드시 어떤 값과 함께 줄 건지 물어보기

    if x:
        radius = radius if radius else 1000
        flag, user_list = get_closer_user(x, y, radius)
        if flag:
            datasets = {'message': '유효하지 않은 요청입니다.'}
            data = json.dumps(datasets, ensure_ascii=False)
            return Response(status=400, data=data, content_type='application.json')
        if not user_list:
            datasets = {'message': '설정한 거리 주변에 등록 된 분실물 관리 센터가 없습니다.'}
            data = json.dumps(datasets, ensure_ascii=False)
            return Response(status=204, data=data, content_type='application.json')
        else:
            posting_set = posting_set.filter(user_id__in=user_list)

    if created_at:
        posting_set = posting_set.filter(created_at__gte=created_at)

    if category:
        posting_set = posting_set.filter(category=category)

    if color:
        posting_set = posting_set.filter(color=color)


    datasets = []
    for posting in posting_set:
        user = posting.user.center_name + posting.user.role

        if posting.has_img:
            img_path = 'media/' + str(get_object_or_404(FoundImage, posting=posting.id).thumbnail)
        else:
            img_path = 'media/no_img.png'

        datasets.append({
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


