from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from datetime import datetime
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth import get_user_model

User = get_user_model()


def found_thumbnail_path(instance, filename):
    filename = datetime.today().strftime('%Y%m%d%H%M%f')
    day = datetime.today().strftime('%Y%m%d')
    return f'found/thumbnail/{day}/{filename}.jpeg'


def found_image_path(instance, filename):
    filename = datetime.today().strftime('%Y%m%d%H%M%f')
    day = datetime.today().strftime('%Y%m%d')
    return f'found/origin/{day}/{filename}.jpeg'


class Color(models.Model):
    color = models.CharField(max_length=20, unique=True)


class Category(models.Model):
    category = models.CharField(max_length=20, unique=True)


class FoundImage(models.Model):
    image = models.ImageField(upload_to=found_image_path)
    category_1 = models.CharField(max_length=20, blank=True)
    category_2 = models.CharField(max_length=20, blank=True)
    category_3 = models.CharField(max_length=20, blank=True)
    numpy_path = models.CharField(max_length=200, blank=True)


class FoundPosting(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='found')

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    status = models.BooleanField()
    content = models.TextField()

    class Meta:
        ordering = ('-created',)


class FoundThumbnail(models.Model):
    posting = models.ForeignKey(FoundPosting, blank=True, null=True, related_name='thumbnail', on_delete=models.CASCADE)
    origin = models.ForeignKey(FoundImage, blank=True, null=True, related_name='thumbnail', on_delete=models.CASCADE)
    image = ProcessedImageField(
        processors=[ResizeToFill(200, 200)],
        upload_to=found_thumbnail_path,
        format='JPEG',
        options={'quality': 90},
    )

    def __str__(self):
        return 'media/%s' % self.image
