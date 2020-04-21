from django.db import models


class Color(models.Model):
    color = models.CharField(max_length=10)


class Category(models.Model):
    category = models.CharField(max_length=10)


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=10)


class Image(models.Model):
    path = models.CharField(max_length=300)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)





