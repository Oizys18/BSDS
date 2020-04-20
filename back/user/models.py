from django.db import models


class Center(models.Model):

    login_id = models.CharField(max_length=20, default=None)
    password = models.CharField(max_length=200, default=None)
    category = models.CharField(max_length=20)
    police_office = models.CharField(max_length=20)
    center_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)


class Address(models.Model):
    center = models.ForeignKey(Center, on_delete=models.CASCADE)

    address_name = models.CharField(max_length=200)
    region_1depth_name = models.CharField(max_length=20)
    region_2depth_name = models.CharField(max_length=20)
    region_3depth_name = models.CharField(max_length=20)
    road_name = models.CharField(max_length=50)
    zone_no = models.CharField(max_length=20)

    x = models.CharField(max_length=50)
    y = models.CharField(max_length=50)
