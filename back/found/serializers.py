from rest_framework import serializers
from .models import FoundPosting, FoundImage, FoundThumbnail
from django.contrib.auth import get_user_model

User = get_user_model()


class FoundImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoundImage
        fields = ('image',)


class FoundPostingSerializer(serializers.ModelSerializer):
    thumbnail = serializers.StringRelatedField(many=True)

    class Meta:
        model = FoundPosting
        fields = ('id', 'color', 'category', 'created', 'modified', 'status', 'thumbnail')


class FoundThumbnailSerializer(serializers.ModelSerializer):
    posting = FoundPostingSerializer()

    class Meta:
        model = FoundThumbnail
        fields = ('posting', 'thumbnail',)


class CreateFoundPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundPosting
        fields = ('category', 'color', 'content')


class CreateFoundThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundThumbnail
        fields = ('thumbnail',)
