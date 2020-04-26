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
    status = models.BooleanField()
    content = models.TextField()

    lostname = models.CharField(max_length=100)
    password = models.CharField(max_length=200)

    email = models.EmailField()
    do_notice = models.BooleanField()
    lost_time = models.DateTimeField(auto_now_add=False)

    class Meta:
        ordering = ('-created',)


class LostThumbnail(models.Model):
    posting = models.ForeignKey(LostPosting, blank=True, null=True, related_name='thumbnail', on_delete=models.CASCADE)
    image = ProcessedImageField(
        processors=[ResizeToFill(200, 200)],
        upload_to=lost_thumbnail_path,
        format='JPEG',
        options={'quality': 90},
    )

    def __str__(self):
        return 'media/%s' % self.image


class LostAddress(models.Model):
    posting = models.ForeignKey(LostPosting, on_delete=models.CASCADE, related_name='address')

    address_name = models.CharField(max_length=200)
    region_1depth_name = models.CharField(max_length=50)
    region_2depth_name = models.CharField(max_length=50)
    region_3depth_name = models.CharField(max_length=50)
    road_name = models.CharField(max_length=50)
    zone_no = models.CharField(max_length=20)

    x = models.CharField(max_length=50)
    y = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % self.address_name
