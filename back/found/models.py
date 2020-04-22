from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django_extensions.db.models import TimeStampedModel

from django.contrib.auth import get_user_model
User = get_user_model()

from ..ai.models import Category, Color


# class FoundPosting(TimeStampedModel):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='found')
#
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='found')
#     color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='posting')
#     status = models.BooleanField()
#     content = models.TextField()
#
#     file = ProcessedImageField(
#         processors=[ResizeToFill(200, 200)],
#         upload_to='found/images',
#         format='JPEG',
#         options={'quality': 80},
#     )
#
#     class Meta:
#         ordering = ('-created',)



