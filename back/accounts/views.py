from django.shortcuts import get_object_or_404, HttpResponse
from .models import User, Address
from rest_framework.decorators import api_view
from rest_framework.response import Response

import json


@api_view(['GET'])
def user_detail(request, user_id):
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


