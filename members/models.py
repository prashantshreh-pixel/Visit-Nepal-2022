from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Photos(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    file = models.ImageField(upload_to='places_photo/')
    description = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'user = {self.user}, title = {self.title}'
