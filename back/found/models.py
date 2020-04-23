from django.db import models
from ai.models import Category, Color
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
    return f'found/{day}/{filename}.jpeg'


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
