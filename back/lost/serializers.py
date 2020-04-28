from rest_framework import serializers
from .models import LostPosting, LostImage, LostThumbnail


class LostImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = LostImage
        fields = ('image',)


class LostThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostThumbnail
        fields = ('image', )


class LostPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostPosting
        fields = ('category', 'color', 'content', 'status',
                  'email', 'do_notice', 'lost_time', 'x', 'y')


class LostPostingDetailSerializer(serializers.ModelSerializer):
    thumbnail = serializers.StringRelatedField(many=True)

    class Meta:
        model = LostPosting
        fields = ('id', 'category', 'status', 'color', 'content', 'email',
                  'do_notice', 'lost_time', 'x', 'y', 'thumbnail')


class AdminLostDetailSerializer(serializers.ModelSerializer):
    thumbnail = serializers.StringRelatedField(many=True)

    class Meta:
        model = LostPosting
        fields = ('id', 'category', 'status', 'color', 'content',
                  'lost_time', 'x', 'y', 'thumbnail')


class AdminLostListSerializer(serializers.ModelSerializer):
    thumbnail = serializers.StringRelatedField(many=True)

    class Meta:
        model = LostPosting
        fields = ('id', 'category', 'status', 'color',
                  'lost_time', 'thumbnail')
