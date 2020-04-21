from django.db import models
from ..ai.models import Category, Color, Image


class Found(models.Model):
    password = models.CharField(max_length=300)
    # lost_date = models.

    # TODO django_advanced insta image 참고하고 datetime field 부터 시작하기
