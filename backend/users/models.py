from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_mobile = models.CharField(max_length=155, null=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    profile_photo = models.ImageField(null=True, blank=True, upload_to='pofile/images/')

    def __str__(self):
        return str(self.user)
