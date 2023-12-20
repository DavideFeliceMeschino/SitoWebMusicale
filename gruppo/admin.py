from django.contrib import admin
from .models import Carousel, Eventi, Artisti, Candidati, Commenti,Foto,Video, PrenotaEvento

# Register your models here.
class CarouselAdmin(admin.ModelAdmin):
    list_display=['titolo','data','luogo','img_preview']
    search_fields =['titolo']
    list_filter =['titolo', 'data']
    readonly_fields=['img_preview']
admin.site.register(Carousel,CarouselAdmin)

class EventiAdmin(admin.ModelAdmin):
    list_display=['titolo','data','luogo','descrizione','img_preview']
    search_fields =['titolo']
    list_filter =['titolo', 'data']
    readonly_fields=['img_preview']
admin.site.register(Eventi,EventiAdmin)

class ArtistiAdmin(admin.ModelAdmin):
    list_display = ['nome','cognome','data_nascita','strumento','email','esperienza','img_preview']
    search_fields =['nome','cognome','strumento']
    list_filter =['strumento']
    readonly_fields=['img_preview']
admin.site.register(Artisti,ArtistiAdmin)

class CandidatiAdmin(admin.ModelAdmin):
    list_display = ['nome','cognome','data_nascita','email','esperienza']
    search_fields =['nome','cognome','strumento']
    list_filter =['strumento']
    
admin.site.register(Candidati,CandidatiAdmin)

class CommentiAdmin(admin.ModelAdmin):
    list_display = ['nome','email','commento']
    search_fields = ['nome','email','commento']
    list_filter = ['nome','email']
admin.site.register(Commenti,CommentiAdmin)

class FotoAdmin(admin.ModelAdmin):
    list_display = ['data_inserimento','img_preview']
admin.site.register(Foto,FotoAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display=['nome','data_inserimento','img_preview']
admin.site.register(Video, VideoAdmin)

class PrenotaEventoAdmin(admin.ModelAdmin):
    list_display=['nome_cliente','cognome_cliente','tipo_evento','data_evento']
admin.site.register(PrenotaEvento,PrenotaEventoAdmin)