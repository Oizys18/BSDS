from django.db import models
# from ai.models import Category, Color
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from datetime import datetime
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth import get_user_model

User = get_user_model()


# def thumbnail_path(instance, filename):
#     filename = datetime.today().strftime('%Y%m%d%H%M%f')
#     day = datetime.today().strftime('%Y%m%d')
#     return f'lost/thumbnail/{day}/{filename}.jpeg'
#
#
# def image_path(instance, filename):
#     filename = datetime.today().strftime('%Y%m%d%H%M%f')
#     day = datetime.today().strftime('%Y%m%d')
#     return f'lost/origin/{day}/{filename}.jpeg'
#
#
# class LostPosting(TimeStampedModel):
#
#     index = models.CharField(max_length=200)
#     email = models.EmailField()
#     password = models.CharField(max_length=200)
#     do_notice = models.BooleanField()
#
#     lost_date_from = models.DateTimeField()
#     lost_date_to = models.DateTimeField()
#
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     color = models.ForeignKey(Color, on_delete=models.CASCADE)
#     status = models.BooleanField()
#
#     content = models.TextField()
#     has_img = models.BooleanField()
#
#     class Meta:
#         ordering = ('-created',)
#
#
# class LostImage(models.Model):
#     posting = models.ForeignKey(LostPosting, on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(upload_to=image_path)
#     thumbnail = ProcessedImageField(
#         processors=[ResizeToFill(200, 200)],
#         upload_to=thumbnail_path,
#         format='JPEG',
#         options={'quality': 90},
#     )


# class LostAddress(models.Model):
#     posting = models.ForeignKey(LostPosting, on_delete=models.CASCADE, related_name='address')
#
#     address_name = models.CharField(max_length=200)
#     region_1depth_name = models.CharField(max_length=50)
#     region_2depth_name = models.CharField(max_length=50)
#     region_3depth_name = models.CharField(max_length=50)
#     road_name = models.CharField(max_length=50)
#     zone_no = models.CharField(max_length=20)
#
#     x = models.CharField(max_length=50)
#     y = models.CharField(max_length=50)
