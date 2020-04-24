from django.shortcuts import get_object_or_404
from .models import User, Address
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import json


@api_view(['GET'])
@permission_classes([AllowAny])
def user_detail(request, user_id):
    """
    User Detail

    return : id, center_name, parent_department(소속된 경찰서), phone_number, address (주소 형식 바꾸는거 가능)
    """
    user = get_object_or_404(User, id=user_id)
    address = get_object_or_404(Address, id=user_id)

    dataset = {
        'id': user_id,
        'center_name': f'{user.center_name} {user.role}',
        'parent_department': user.parent_department,
        'phone_number': user.phone_number,
        'address': address.address_name,
    }

    res_data = json.dumps(dataset, ensure_ascii=False)
    return Response(status=200, data=res_data, content_type='application/json')
