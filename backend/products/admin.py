from django.contrib import admin
from django.utils.safestring import mark_safe
from rangefilter.filters import NumericRangeFilter, NumericRangeFilterBuilder

from .models import Product, Category, Photo, Cart, CartProduct


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ('show_photo', 'name', 'price', 'category',)
    list_display_links = ('name', 'price', 'category')
    list_filter = (('price', NumericRangeFilterBuilder()),)
    search_fields = ('name', 'category__name')
    read_only_fields = ['show_photo']

    def show_photo(self, obj):
        photo = obj.photos.first()
        default_photo_path = '/media/product/photos/default.png'
        if photo:
            return mark_safe(f'<img src="{photo.image.url}" style="width: 84px; height:75px;" />')

        return mark_safe(f'<img src="{default_photo_path}" style="width: 84px; height:75px;" />')


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('product', 'image',)
    search_fields = ('product', 'image')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('owner',)


@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    @admin.action(description='Cancel product order')
    def cancel_product_order(self, request, queryset):
        queryset.update(ordering=False)

    @admin.action(description='Order a product')
    def order_product(self, request, queryset):
        queryset.update(ordering=True)

    list_display = ('cart', 'product', 'quantity', 'ordering')
    search_fields = ('product',)
    list_filter = ('ordering',)
    actions = ('cancel_product_order', 'order_product')
