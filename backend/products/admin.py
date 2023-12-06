from django.contrib import admin

from .models import Product, Category, Photo, Cart, CartProduct


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Cart)
admin.site.register(CartProduct)
