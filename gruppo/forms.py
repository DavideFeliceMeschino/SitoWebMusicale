from django import forms 

from .models import Artisti


class CandidatiForm(forms.ModelForm):
    class Meta:
        model = Artisti
        fields = ['nome','cognome','data_nascita','email','esperienza']