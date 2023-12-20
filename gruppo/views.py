from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Carousel,Eventi, Artisti,Commenti,Foto
from .forms import CandidatiForm, CommentiForm

# Create your views here.
def home(request):
    slides = Carousel.objects.all()
    eventi = Eventi.objects.all()
    return render(request, 'home.html',{'slides':slides,'eventi':eventi})

def fotopage(request):
    foto = Foto.objects.all()
    return render(request, 'fotopage.html', {'foto':foto,})

def videopage(request):
    return render(request, 'videopage.html', {})

def chisiamo(request):
    artisti = Artisti.objects.all()
    return render(request, 'chisiamo.html',{'artisti':artisti})

def lavoraconnoi(request):
    if request.method == 'POST':
        form = CandidatiForm(request.POST)
        if form.is_valid():
            candidato = form.save()
            return redirect('gruppo:home')
    else:
        form = CandidatiForm()
    return render(request, 'lavoraconnoi.html', {'form':form})

def prenotaevento(request):
    return render(request, 'prenotaevento.html', {})