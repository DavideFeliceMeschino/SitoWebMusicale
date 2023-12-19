from django.contrib import admin
from .models import Carousel

# Register your models here.
class CarouselAdmin(admin.ModelAdmin):
    list_display=['titolo','data','luogo','img_preview']
admin.site.register(Carousel)