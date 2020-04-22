from django.db import models


class Color(models.Model):
    color = models.CharField(max_length=20, unique=True)


class Category(models.Model):
    category = models.CharField(max_length=20, unique=True)


# class Image(models.Model):
#     path = models.CharField(max_length=300)
#     color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='images')
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='images')





