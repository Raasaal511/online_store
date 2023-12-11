from django.contrib import admin

from .models import Product, Category, Photo, Cart, CartProduct


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


admin.site.register(Photo)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartProduct)
