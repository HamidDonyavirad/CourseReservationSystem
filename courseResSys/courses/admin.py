from django.contrib import admin
from .models import Reservation, Course
from django.contrib.auth import get_user_model
from django.utils.html import format_html
# Register your models here.
admin.site.register(get_user_model())

admin.site.register(Reservation)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return 'No Image'

    image_preview.short_description = 'Preview'
    
admin.site.register(Course, ProductAdmin)