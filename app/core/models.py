# from django.db import models

# # Create your models here.
# from django.contrib.auth.models import (
#     AbstractBaseUser,
#     BaseUserManager,
#     PermissionsMixin,
# )

# class UserManager(BaseUserManager):
#     """manger user for manager"""
#     def create_user(self, email,password=None,**extra_fields):
#         """create safe and return a new user"""
#         if not email:
#             raise ValueError('user must have an email address')

#         user=self.model(email=self.normalize_email(email),**extra_fields)
#         user.set_password(password)

#         user.save(using=self._db)

#         return user

#     def create_superuser(self, email,password):
#         """create and return a new super user"""
       
#         user=self.create_user(email,password)
#         user.is_staff=True
#         user.is_superuser=True
       

#         user.save(using=self._db)

#         return user



# class User(AbstractBaseUser,PermissionsMixin):
#     """"user in the system"""
#     email=models.EmailField(max_length=225, unique=True)
#     name=models.CharField(max_length=225)
#     is_active=models.BooleanField(default=True)
#     is_staff=models.BooleanField(default=False)

#     USERNAME_FIELD='email'
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=225, unique=True)
    name = models.CharField(max_length=225)
    first_name = models.CharField(max_length=225,default='')
    last_name = models.CharField(max_length=225,default='')
    username = models.EmailField(max_length=225,default='')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()  # Use the custom user manager

    USERNAME_FIELD = 'email'
