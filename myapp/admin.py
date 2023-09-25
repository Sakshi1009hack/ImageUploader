from django.contrib import admin

# Register your models here.
from.models import Image
@admin.register(Image)
class Imageadmin(admin.ModelAdmin):
    list_display=['id','photo','date']
    