from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    imageUrl = models.ImageField(upload_to='profile', default='profile/avatar_female.jpg')


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


class Post(models.Model):
    title = models.CharField(max_length=150)
    # description = models.TextField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # def likes_count(self):
    #     return self.likes.all().count()
    #
    # def __str__(self):
    #     return '%s' % self.title


class Like(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

# learn


class Collection(models.Model):
    title = models.CharField(max_length=255)


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)