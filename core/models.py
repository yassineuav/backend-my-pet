from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    bio = models.TextField()
    imageUrl = models.ImageField(upload_to='profile', default='')


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    zip = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Adaption(models.Model):
    desc = models.CharField(max_length=255)
    title = models.CharField(max_length=30)
    datetime = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')


class InterestedIn(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    popular = models.IntegerField(default=0)
    usersIn = models.IntegerField(default=0)
    suggestedTimes = models.IntegerField(default=0)
    display = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    imageUrl = models.ImageField(upload_to='interested/images', default='')
    iconUrl = models.ImageField(upload_to='interested/icons', default='')


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    description = models.TextField()
    imageUrl = models.ImageField(upload_to='post/images', default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

