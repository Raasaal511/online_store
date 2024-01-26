from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=155, null=True, blank=True)

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_photo = models.ImageField(null=True, blank=True, upload_to='pofile/images/')

    def __str__(self):
        return str(self.user)
