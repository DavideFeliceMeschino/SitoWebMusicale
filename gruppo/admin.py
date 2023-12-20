from django.contrib import admin
from .models import Carousel, Eventi, Artisti, Candidati

# Register your models here.
class CarouselAdmin(admin.ModelAdmin):
    list_display=['titolo','data','luogo','img_preview']
admin.site.register(Carousel)

class EventiAdmin(admin.ModelAdmin):
    list_display=['titolo','data','luogo','descrizione','img_preview']
admin.site.register(Eventi)

class ArtistiAdmin(admin.ModelAdmin):
    list_display = ['nome','cognome','data_nascita','strumento','email','esperienza','img_preview']
admin.site.register(Artisti)

class CandidatiAdmin(admin.ModelAdmin):
    list_display = ['nome','cognome','data_nascita','email','esperienza']
admin.site.register(Candidati)