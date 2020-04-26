from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, username, parent_department, role, center_name, phone_number, password=None):
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
            parent_department=parent_department,
            role=role,
            center_name=center_name,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, parent_department, role, center_name, phone_number, password=None):
        user = self.create_user(
            username,
            parent_department=parent_department,
            role=role,
            center_name=center_name,
            phone_number=phone_number,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True)

    parent_department = models.CharField(max_length=30)
    role = models.CharField(max_length=20)
    center_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['parent_department', 'role', 'center_name', 'phone_number']

    def __str__(self):
        return '%s%s' % (self.center_name, self.role)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Address(models.Model):
    center = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address')

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
