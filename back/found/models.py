from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from datetime import datetime
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth import get_user_model

User = get_user_model()


def thumbnail_path(instance, filename):
    filename = datetime.today().strftime('%Y%m%d%H%M%f')
    day = datetime.today().strftime('%Y%m%d')
    return f'found/thumbnail/{day}/{filename}.jpeg'


def image_path(instance, filename):
    filename = datetime.today().strftime('%Y%m%d%H%M%f')
    day = datetime.today().strftime('%Y%m%d')
    return f'found/origin/{day}/{filename}.jpeg'


class Color(models.Model):
    color = models.CharField(max_length=20, unique=True)

#TODO 여기부터 ~~~~~~~~~~~~~ 디비 문제 수정하기 부터~~~~~~~~~
class Category(models.Model):
    category = models.CharField(max_length=20, unique=True)


class FoundPosting(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='found')

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    status = models.BooleanField()

    content = models.TextField()
    has_img = models.BooleanField()

    class Meta:
        ordering = ('-created',)


class FoundImage(models.Model):
    posting = models.ForeignKey(FoundPosting, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=image_path)
    thumbnail = ProcessedImageField(
        processors=[ResizeToFill(200, 200)],
        upload_to=thumbnail_path,
        format='JPEG',
        options={'quality': 90},
    )
