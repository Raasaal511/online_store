from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from products.models import Product, Category


# class ProductAPITest(APITestCase):
#     def setUp(self):
#         Category.objects.create(name='category')

    # def test_product_create(self):
    #     cat = Category.objects.get(name='category')
    #     data = {
    #         "name": "Product",
    #         "description": "Product desc.",
    #         "price": 15.9,
    #         "category": {'name': cat.name},
    #         "photos": {'image': None},
    #     }
    #     url = reverse('product-list')
    #     response = self.client.post(url, data, format='json')
    #
    #     self.assertEquals(response.status_code,  status.HTTP_201_CREATED)
    #     self.assertEquals(Product.objects.get(name='Product').name, 'Product')
    #

