from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .models import LostPosting, LostImage, LostThumbnail, LostAddress
from .serializers import LostImageSerializer, LostThumbnailSerializer, CreateLostPostingSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
import json
from decouple import config
import requests
from django.views.decorators.cache import cache_page

from django.contrib.auth import get_user_model
User = get_user_model()


@api_view(['POST'])
@permission_classes([AllowAny])
def create_lost_image(request):
    if request.FILES:
        serializer = LostImageSerializer(request.POST, request.FILES)
        if serializer.is_valid():
            th_serializer = LostThumbnailSerializer(request.POST, request.FILES)
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
@permission_classes([AllowAny])
def create_lost(request):
    data = {
        'image_id': 3,
        'color': 3,
        'category': 2,
        'content': ''
    }

    serializer = CreateLostPostingSerializer(data=data)
    if serializer.is_valid():
        # 비밀번호 암호화
        # lost_time error 확인하기
        posting = serializer.save(status=False)

        if data["image_id"]:
            thumbnail = get_object_or_404(LostThumbnail, id=data["image_id"])
            thumbnail.posting_id = posting.id
            thumbnail.save()

        return Response(status=200, data=serializer.data)
    return Response(status=400, data={'message': 'Invalid input'})


@api_view(['POST'])
@permission_classes([AllowAny])
def lost_login(request):
    pass


@api_view(['PATCH', 'DELETE'])
@permission_classes([AllowAny])
def update_delete_lost(request, lost_id):
    pass


@api_view(['PATCH'])
@permission_classes([AllowAny])
def update_lost_status(request, lost_id):
    pass


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_lost_list_admin(request):
    pass


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_lost_detail_admin(request, lost_id):
    pass


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def send_lost_notice(request, lost_id):
    pass

