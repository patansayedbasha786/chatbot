

# Register your models here.
from django.contrib import admin
from .models import ImageRecord


@admin.register(ImageRecord)
class ImageRecordAdmin(admin.ModelAdmin):
    list_display = ("title", "category")
    search_fields = ("title", "category")