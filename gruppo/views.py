from django.shortcuts import render
from .models import Carousel

# Create your views here.
def home(request):
    slides = Carousel.objects.all()
    return render(request, 'home.html',{'slides':slides})

def fotopage(request):
    return render(request, 'fotopage.html', {})

def videopage(request):
    return render(request, 'videopage.html', {})

def chisiamo(request):
    return render(request, 'chisiamo.html',{})

def lavoraconnoi(request):
    return render(request, 'lavoraconnoi.html', {})

def prenotaevento(request):
    return render(request, 'prenotaevento.html', {})