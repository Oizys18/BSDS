from rest_framework import serializers
from .models import FoundPosting, FoundImage, FoundThumbnail
from django.contrib.auth import get_user_model
User = get_user_model()


class FoundImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoundImage
        fields = 'image'


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


class FoundPostingListSerializer(serializers.ModelSerializer):
    thumbnail = FoundThumbnailSerializer()
    # user = UserSerializer()

    class Meta:
        model = FoundPosting
        fields = ('thumbnail', 'created', 'modified',)


class FoundThumbnailListSerializer(serializers.ModelSerializer):
    posting = FoundPostingListSerializer()

    class Meta:
        model = FoundThumbnail
        fields = ('posting', 'thumbnail',)
