from django.shortcuts import get_object_or_404
from .models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserInfoSerializer



@api_view(['GET'])
@permission_classes([AllowAny])
def user_detail(request, user_id):

    user = get_object_or_404(User, id=user_id)
    serializer = UserInfoSerializer(user)

    return Response(status=200, data=serializer.data, content_type='application/json')
