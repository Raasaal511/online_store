from pathlib import Path

from django.test import TestCase
from django.utils.text import slugify

from products.models import Product, Category, Photo, Cart, CartProduct
from django.core.files.uploadedfile import SimpleUploadedFile


class ProductTest(TestCase):
    def setUp(self):
        cat = Category.objects.create(name='category')
        product = Product.objects.create(
            name='product',
            description='product desc',
            price=20.10,
            category=cat,
        )
        return product

    def test_update(self):
        product = Product.objects.get(name='product')
        product.price = 10.01
        self.assertEquals(product.price, 10.01)

    def test_delete(self):
        Product.objects.get(name='product').delete()
        self.assertFalse(Product.objects.filter(name='product').exists())

    def test_slugify(self):
        product = Product.objects.get(name='product')
        self.assertEquals(product.slug, slugify(product.name))


class CategoryTest(TestCase):

    def setUp(self):
        category = Category.objects.create(name='category')
        return category

    def test_create(self):
        category = Category.objects.create(name='category')
        self.assertEquals(category.name, 'category')

    def test_update(self):
        category = Category.objects.update(name='new_category')
        self.assertEquals(category, 1)

    def test_delete(self):
        category = Category.objects.filter(name='category')
        category.delete()
        self.assertFalse(category.exists())

    def test_read(self):
        category = Category.objects.get(name='category')
        self.assertEquals(category.name, 'category')


class PhotoTest(TestCase):
    def setUp(self):
        cat = Category.objects.create(name='category')
        self.product = Product.objects.create(
            name='product',
            description='product desc',
            price=20.10,
            category=cat,
        )
        self.new_product = Product.objects.create(
            name='product1',
            description='product desc1',
            price=20.11,
            category=cat,
        )
        self.test_image_path = (
                Path(__file__).resolve().parent.parent / "media/product/photos/images.png"
        )

    def test_create(self):
        photo = Photo.objects.create(product=1, image=self.test_image_path)
        self.assertEquals(photo.product, 1)
        self.assertEquals(photo.image, 'image.png')

    def test_update(self):
        new_image = (
                Path(__file__).resolve().parent.parent / "media/product/photos/default.png"
        )
        print(self.get_image())
        photo = Photo.objects.update(product=self.new_product, image=self.get_image())
        self.assertEquals(photo, 1)

    def test_delete(self):
        photo = Photo.objects.filter(image=self.test_image_path)
        print(photo)
        photo.delete()
        self.assertFalse(photo.exists())

    def test_read(self):
        photo = Photo.objects.get(image=self.test_image_path)
        self.assertEquals(photo.image, 'images.png')


class CartTest(TestCase):
    pass


class CartProductTest(TestCase):
    pass
