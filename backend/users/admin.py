from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import User, Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number')
    search_fields = ('username', 'email', 'phone_number')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('default_photo', 'user')
    search_fields = ('user__email',)

    def default_photo(self, obj):
        photo = obj.profile_photo
        default_photo_path = '/media/product/photos/default.png'
        if photo:
            return mark_safe(f'<img src="{photo.image.url}" style="width: 84px; height:75px;" />')

        return mark_safe(f'<img src="{default_photo_path}" style="width: 84px; height:75px;" />')
