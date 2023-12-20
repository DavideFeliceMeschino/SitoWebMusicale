from django import forms 
from captcha.fields import CaptchaField

from .models import Artisti,Candidati,Commenti


class CandidatiForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Candidati
        fields = ['nome','cognome','data_nascita','email','strumento','esperienza','captcha']

    def __init__(self, *args, **kwargs):
        super(CandidatiForm, self).__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs['class'] = 'form-group'            
        self.fields['nome'].label = 'Nome'

        self.fields['cognome'].widget.attrs['class'] = 'form-group'            
        self.fields['cognome'].label = 'Cognome'

        self.fields['data_nascita'].widget.attrs['class'] = 'form-group'            
        self.fields['data_nascita'].label = 'Data di Nascita'

        self.fields['email'].widget.attrs['class'] = 'form-group'            
        self.fields['email'].label = 'Email'

        self.fields['strumento'].widget.attrs['class'] = 'form-group'            
        self.fields['strumento'].label = 'Strumento'

        self.fields['esperienza'].widget.attrs['class'] = 'form-group'            
        self.fields['esperienza'].label = 'Esperienza Lavorativa'


class CommentiForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Commenti
        fields = ['nome','email','commento','captcha']   
        