from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .models import LostPosting, LostImage, LostThumbnail, LostAddress
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
    pass


@api_view(['POST'])
@permission_classes([AllowAny])
def create_lost(request):
    pass


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

