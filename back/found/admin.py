from django.contrib import admin
from .models import FoundPosting, FoundImage


class FoundPostingModelAdmin(admin.ModelAdmin):
    list_display = 'id', 'category'


class FoundImageModelAdmin(admin.ModelAdmin):
    list_display = 'id', 'image'


admin.site.register(FoundPosting, FoundPostingModelAdmin)
admin.site.register(FoundImage, FoundImageModelAdmin)
