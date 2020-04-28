from django.db import models
from found.models import Category, Color
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from datetime import datetime
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth import get_user_model

User = get_user_model()


def lost_thumbnail_path(instance, filename):
    filename = datetime.today().strftime('%Y%m%d%H%M%f')
    day = datetime.today().strftime('%Y%m%d')
    return f'lost/thumbnail/{day}/{filename}.jpeg'


def lost_image_path(instance, filename):
    filename = datetime.today().strftime('%Y%m%d%H%M%f')
    day = datetime.today().strftime('%Y%m%d')
    return f'lost/origin/{day}/{filename}.jpeg'


class LostImage(models.Model):
    image = models.ImageField(upload_to=lost_image_path)
    category_1 = models.CharField(max_length=20, blank=True)
    category_2 = models.CharField(max_length=20, blank=True)
    category_3 = models.CharField(max_length=20, blank=True)
    numpy_path = models.CharField(max_length=200, blank=True)


class LostPosting(TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    status = models.BooleanField(blank=True)
    content = models.TextField(blank=True)

    lostname = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=200, blank=True)

    email = models.EmailField()
    do_notice = models.BooleanField()
    lost_time = models.DateTimeField(auto_now_add=False)

    x = models.CharField(max_length=50, blank=True, null=True)
    y = models.CharField(max_length=50, blank=True, null=True)

    p1 = models.IntegerField(blank=True, null=True)
    p2 = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ('-lost_time',)


class LostThumbnail(models.Model):
    posting = models.ForeignKey(LostPosting, blank=True, null=True, related_name='thumbnail', on_delete=models.CASCADE)
    origin = models.ForeignKey(LostImage, blank=True, null=True, related_name='thumbnail', on_delete=models.CASCADE)
    image = ProcessedImageField(
        processors=[ResizeToFill(200, 200)],
        upload_to=lost_thumbnail_path,
        format='JPEG',
        options={'quality': 90},
    )

    def __str__(self):
        return 'media/%s' % self.image

