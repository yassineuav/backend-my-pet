from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_STATUS_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female')]
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    bio = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER_STATUS_CHOICES, default=GENDER_FEMALE)
    imageUrl = models.ImageField(upload_to='profile', default='profile/avatar_female.jpg')


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
    UPLOAD_FROM_ANDROID = 'A'
    UPLOAD_FROM_IPHONE = 'I'
    UPLOAD_FROM_WEBAPP = 'W'
    UPLOAD_FROM_STATUS_CHOICES = [
        (UPLOAD_FROM_ANDROID, 'Android'),
        (UPLOAD_FROM_IPHONE, 'Iphone'),
        (UPLOAD_FROM_WEBAPP, 'WebApp')
    ]
    uploaded_from = models.CharField(max_length=1, choices=UPLOAD_FROM_STATUS_CHOICES, default=UPLOAD_FROM_WEBAPP)

    CONTENT_TYPE_IMAGE = 'I'
    CONTENT_TYPE_VIDEO = 'V'
    CONTENT_TYPE_STATUS_CHOICES = [
        (CONTENT_TYPE_IMAGE, 'image'),
        (CONTENT_TYPE_VIDEO, 'video')
    ]
    content_type = models.CharField(max_length=1, choices=CONTENT_TYPE_STATUS_CHOICES, default=CONTENT_TYPE_IMAGE)

    description = models.TextField()
    imageUrl = models.ImageField(upload_to='post/images', default='')
    usersIn = models.IntegerField(default=0)
    suggestedTimes = models.IntegerField(default=0)
    display = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Like(models.Model):
    user_id = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')


class Tags(models.Model):
    tag = models.CharField(max_length=255)
    suggestedTimes = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)


class Views(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    viewed_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
