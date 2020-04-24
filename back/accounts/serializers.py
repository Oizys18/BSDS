from rest_framework import serializers
from .models import Address
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


# class AddressSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Address
#         fields =


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'parent_department', 'role', 'center_name', 'phone_number')