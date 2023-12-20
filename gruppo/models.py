from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

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
    

class Video(models.Model):
    nome = models.CharField(max_length=150, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    data_inserimento = models.DateTimeField(auto_now_add=True)
    data_modifica = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='img_video/%Y/%m/%d/', default='no-image.png')
    img_resized = ImageSpecField(source='img',processors=[ResizeToFit(250,250)],format='PNG',options={'quality': 60})

    def __str__(self):
        return f"{self.nome}"
    

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
    commento = models.CharField(max_length=250)    
    

    def __str__(self):
        return (f"{self.nome}" f"{self.commento}...")
    

class PrenotaEvento(models.Model):
    ARTIST_TYPE_CHOICE = (
        ('cantante','Cantante'),
        ('deejay','Deejay'),
        ('animatrica','Animatrice'),
        ('presentatore','Presentatore'),
        ('sax','Sax'),
        ('violino','Violino'),
        ('tastiera','Tastiera'),
        ('bassisat','Bassista'),
        ('percussioni','Percussioni'),
        ('batteria','Batteria')
    )
    nome_cliente = models.CharField(max_length=150, null=True, blank=True)
    cognome_cliente = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=255)
    citta = models.CharField(max_length=150, null=True, blank=True)
    provincia =models.CharField("Sigla provincia di residenza", max_length=2, blank=True, null=True, validators=[RegexValidator(
        regex=r'^[A-Za-z]{2}$',
        message='Inserisci la sigla di una provincia (2 lettere)',
    )])
    telefono = models.CharField("Cellulare contatto", max_length=15, blank=True, null=True, validators=[RegexValidator(
        regex=r'^\d{,15}$',
        message='Inserisci un numero di cellulare (solo cifre, senza spazi)',
    )])
    tipo_evento = models.CharField("Tipo di evento (matrimonio, compleanno...)",max_length=150, null=True, blank=True)
    luogo = models.CharField("Luogo/nome della sala",max_length=255, null=True, blank=True)
    citta_evento = models.CharField("Città dell'evento", max_length=200)
    prov_evento = models.CharField("Sigla provincia dell'evento", max_length=2, blank=True, null=True, validators=[RegexValidator(
        regex=r'^[A-Za-z]{2}$',
        message='Inserisci la sigla di una provincia (2 lettere)',
    )])
    indirizzo_evento = models.CharField("Via/Piazza e numero civico",max_length=255, null=True, blank=True)
    seleziona_artisti = models.CharField('Seleziona artisti',max_length=50,default=' ',choices=ARTIST_TYPE_CHOICE)
    data_evento  = models.DateTimeField()