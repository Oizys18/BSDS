from rest_framework import serializers
from .models import LostPosting, LostImage


class LostPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostPosting
        fields = ('id', 'content', 'status', 'has_img')


class LostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostImage
        fields = ('image', 'thumbnail')


# class LostAddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LostAddress
#         fields = ('x', 'y')
#
