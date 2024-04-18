from django.db import models
from django_extensions.db.fields import AutoSlugField


class Category(models.Model):
    name = models.CharField(max_length=155)
    slug = AutoSlugField(unique=True, blank=True, null=True, populate_from='name')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=155)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='category')
    slug = AutoSlugField(unique=True, blank=True, null=True, populate_from='name')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-pk']


# class BaseImage(models.Model):
#     """Basic model for images"""
#     title = models.CharField(max_length=200, null=True, blank=True)
#     alt = models.CharField(max_length=200, null=True, blank=True)
#     image = VersatileImageField(null=True, blank=True, upload_to='images')
#
#     class Meta:
#         abstract = True
#         verbose_name = "Image"
#         verbose_name_plural = "Images"

    # def __str__(self):
    #     res = ''
    #     if self.title:
    #         res = self.title
    #     else:
    #         res = self.image.url
    #     return res

class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='photos')
    image = models.ImageField(upload_to='product/photos/', default='product/default.png', null=True, blank=True)

    def __str__(self):
        return self.image.url


class Cart(models.Model):
    owner = models.OneToOneField(to='users.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.owner.username


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    quantity = models.PositiveIntegerField(default=1)
    ordering = models.BooleanField(default=True)

