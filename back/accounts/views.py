from django.shortcuts import get_object_or_404
from .models import User, Address
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserInfoSerializer
import json


@api_view(['GET'])
@permission_classes([AllowAny])
def user_detail(request, user_id):
    """
    User Detail

    return : id, center_name, role, parent_department(소속된 경찰서), phone_number, address (주소 형식 바꾸는거 가능)
    """
    user = get_object_or_404(User, id=user_id)
    serializer = UserInfoSerializer(user)

    return Response(status=200, data=serializer.data, content_type='application/json')
