from rest_framework import serializers
from .models import LostPosting, LostImage, LostThumbnail, LostAddress


class LostImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = LostImage
        fields = ('image',)


class LostThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostThumbnail
        fields = ('image',)


class LostPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostPosting
        fields = ('category', 'color', 'content',
                  'email', 'do_notice', 'lost_time', 'x', 'y')


class LostPostingDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = LostPosting
        fields = ('id', 'category', 'color', 'content', 'email',
                  'do_notice', 'lost_time', 'x', 'y')
