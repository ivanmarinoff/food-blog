from django.contrib import admin
from django.utils.html import format_html

from .models import Blog



class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "image_url", "summary", "image_tag"]
    list_filter = ["title", "category"]
    search_fields = ['title']
    ordering = ['-title']

    def image_tag(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" style="max-width:150px; max-height:150px"/>'.format(obj.image_url))
        return None






admin.site.register(Blog, imageAdmin)