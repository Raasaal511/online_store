from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=155)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=155)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-pk']


class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='photos', null=True, blank=True)
    image = models.ImageField(upload_to='product/photos/', null=True, blank=True)

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

