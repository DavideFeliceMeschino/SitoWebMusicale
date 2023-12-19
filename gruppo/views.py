from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html',{})

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