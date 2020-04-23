from rest_framework import serializers
from .models import FoundPosting, FoundImage

from django.core.serializers.json import DjangoJSONEncoder


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        # if isinstance(obj, YourCustomType):
        #     return str(obj)
        return super().default(obj)


class FoundPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundPosting
        fields = ('id', 'content', 'status', 'has_img')


class FoundImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundImage
        fields = ('image', 'thumbnail')
