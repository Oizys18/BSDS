from django.contrib import admin
from .models import FoundPosting, FoundImage, FoundThumbnail, Category, Color


class FoundPostingModelAdmin(admin.ModelAdmin):
    list_display = 'id', 'category'


class FoundImageModelAdmin(admin.ModelAdmin):
    list_display = 'id', 'image'


class FoundThumbnailModelAdmin(admin.ModelAdmin):
    list_display = 'id', 'image'


class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['color']


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['category']


admin.site.register(FoundPosting, FoundPostingModelAdmin)
admin.site.register(FoundImage, FoundImageModelAdmin)
admin.site.register(FoundThumbnail, FoundThumbnailModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Color, ColorModelAdmin)
