from django.db import models

#Per immagine preview in admin
from django.utils.html import mark_safe
#Librerie per Resize Img
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToCover

# Create your models here.

class Carousel(models.Model):
    titolo = models.CharField("Evento",max_length=200)
    data = models.CharField("Data", max_length=200)
    luogo =models.CharField("Luogo", max_length=200)
    img = models.ImageField("Immagine Slide", upload_to='slide/%Y/%m/%d', default='static/slide/no_img.jpeg')

    def __str__(self):
        return self.titolo
    
    def img_preview(self):
        return mark_safe(f'<img src="{self.img.url}" width=150/>')

