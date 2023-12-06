from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Cart


@receiver(post_save, sender=settings.AUTH_USER_MDOEL)
def create_user_cart(sender, created, instance, **kwargs):
    if created:
        Cart.objects.create(owner=instance)
