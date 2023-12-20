from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Carousel,Eventi, Artisti
from .forms import CandidatiForm

# Create your views here.
def home(request):
    slides = Carousel.objects.all()
    eventi = Eventi.objects.all()
    return render(request, 'home.html',{'slides':slides,'eventi':eventi})

def fotopage(request):
    eventi = Eventi.objects.all()
    return render(request, 'fotopage.html', {'eventi':eventi})

def videopage(request):
    return render(request, 'videopage.html', {})

def chisiamo(request):
    artisti = Artisti.objects.all()
    return render(request, 'chisiamo.html',{'artisti':artisti})

def lavoraconnoi(request):
    if request.method == 'POST':
        form = CandidatiForm(request.POST)
        if form.is_valid():
            artista = form.save()
            messages.success(request,("La tua candidatura è sata inviata con sucesso"))
            return redirect('home')
    else:
        form = CandidatiForm()
    return render(request, 'lavoraconnoi.html', {'form':form})

def prenotaevento(request):
    return render(request, 'prenotaevento.html', {})