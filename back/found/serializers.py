from rest_framework import serializers
from .models import FoundPosting, FoundImage
from django.contrib.auth import get_user_model

User = get_user_model()

from django.core.serializers.json import DjangoJSONEncoder


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        # if isinstance(obj, YourCustomType):
        #     return str(obj)
        return super().default(obj)


class FoundPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundPosting
        fields = ('id', 'color', 'category', 'content', 'status')


class FoundImageSerializer(serializers.ModelSerializer):
    posting = FoundPostingSerializer()

    class Meta:
        model = FoundImage
        fields = ('thumbnail', 'posting')

