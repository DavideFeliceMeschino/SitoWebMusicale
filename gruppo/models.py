from django.db import models

#Per immagine preview in admin
from django.utils.html import mark_safe
#Librerie per Resize Img
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToCover, ResizeToFit

# Create your models here.

class Carousel(models.Model):
    titolo = models.CharField("Evento",max_length=200)
    data = models.CharField("Data", max_length=200)
    luogo =models.CharField("Luogo", max_length=200)
    img = models.ImageField("Immagine Slide", upload_to='slide/%Y/%m/%d', default='media/logo.png')
    img_resize = ImageSpecField(source='img', processors=[ResizeToFit(400,400)], format='PNG', options={'quality': 50})

    def __str__(self):
        return self.titolo
    
    def img_preview(self):
        return mark_safe(f'<img src="{self.img.url}" width=150/>')


class Eventi(models.Model):
    titolo = models.CharField(max_length=255)
    data = models.DateTimeField()
    luogo = models.CharField(max_length=255)
    descrizione = models.TextField()
    img = models.ImageField("Immagine Evento", upload_to='img_evento/%Y/%m/%d', default='media/logo.png')
    img_resize = ImageSpecField(source='img', processors=[ResizeToFit(50,50)], format='PNG', options={'quality': 50})

    def __str__(self):
        return self.titolo
    
    def img_preview(self):
        return mark_safe(f'<img src="{self.img.url}" width=150/>')
       
    
    

class Artisti(models.Model):
    nome = models.CharField(max_length=200)
    cognome = models.CharField(max_length=200)
    data_nascita = models.DateField('Data di nascita')
    strumento = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    esperienza = models.TextField()
    img = models.ImageField('Foto Profilo', upload_to='img_artisti', blank=True,null=True)
    img_resize =ImageSpecField(source='img', processors=[ResizeToFit(150,150)], format='PNG',options={'quality':50})

    def __str__(self):
        return f'{self.nome} {self.cognome}'
    
    def img_preview(self):
        return mark_safe(f'<img src="{self.img.url}" width=150/>')
    
class Foto(models.Model):
    data_inserimento=models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='img_fotopage/%Y/%m/%d', default='logo.png')
    img_resize = ImageSpecField(source='img', processors=[ResizeToFit(250,250)],format='PNG',options={'quality':60})

    def __str__(self):
        return f"{self.img.url}"
    

    def img_preview(self):
        return mark_safe(f'<img src="{self.img.url}" width="150" />')


class Candidati(models.Model):
    nome = models.CharField(max_length=200)
    cognome = models.CharField(max_length=200)
    data_nascita = models.DateTimeField()
    email = models.EmailField(max_length=200)
    esperienza = models.TextField()
    strumento = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nome} {self.cognome}'

class Commenti(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    commento = models.TextField()
    

    def __str__(self):
        return (f"{self.nome}" f"({self.creato_il: %Y-%m-%d %H:%M}): " f"{self.commento}...")