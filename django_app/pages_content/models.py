from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    Category = models.CharField(max_length=30)

    def __str__(self):
        return self.Category


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    description = models.TextField(max_length=5000, null=False)
    post_date = models.DateTimeField(auto_now_add=True)
    Category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cmt = models.TextField(max_length=2000)
    timestamp = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        return f'{self.user.username}: {self.cmt[:20]}'
