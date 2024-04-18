from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Cart, Product, Photo


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_cart(sender, created, instance, **kwargs):
    if created:
        Cart.objects.create(owner=instance)
