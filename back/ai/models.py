from django.db import models


class Color(models.Model):
    color = models.CharField(max_length=20, unique=True)


class Category(models.Model):
    category = models.CharField(max_length=20, unique=True)







