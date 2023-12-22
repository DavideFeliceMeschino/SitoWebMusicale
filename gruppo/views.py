from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Carousel,Eventi, Artisti,Commenti,Foto,Video
from .forms import CandidatiForm, CommentiForm,PrenotaEventiForm

# Create your views here.
def home(request):
    slides = Carousel.objects.all()
    eventi = Eventi.objects.all().order_by('data')
    return render(request, 'home.html',{'slides':slides,'eventi':eventi})

def fotopage(request):
    foto = Foto.objects.all().order_by('data_inserimento')

    form=CommentiForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            commenti=form.save()
            return redirect('gruppo:foto')
    else:
       form =CommentiForm()
    commenti = Commenti.objects.all().order_by('id')
    return render (request, 'fotopage.html',{'foto':foto,'form':form,'commenti':commenti})

    
    

def videopage(request):
    video = Video.objects.all()
    form=CommentiForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            commenti=form.save()
            return redirect('gruppo:video')
    else:
       form =CommentiForm()
       commenti = Commenti.objects.all()
    return render (request, 'videopage.html',{'form':form,'commenti':commenti, 'video':video})
    

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
    if request.method == 'POST':
        form = PrenotaEventiForm(request.POST)
        if form.is_valid():
            prenotaevento = form.save()
            return redirect('gruppo:home')
    else:
        form = PrenotaEventiForm()
    return render(request, 'prenotaevento.html', {'form':form})