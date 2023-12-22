from django import forms 
from captcha.fields import CaptchaField

from .models import Artisti,Candidati,Commenti,PrenotaEvento


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

class PrenotaEventiForm(forms.ModelForm):
    captcha = CaptchaField() 
    seleziona_artista = forms.MultipleChoiceField(
        choices=[('cantante','Cantante'),
        ('deejay','Deejay'),
        ('animatrica','Animatrice'),
        ('presentatore','Presentatore'),
        ('sax','Sax'),
        ('violino','Violino'),
        ('tastiera','Tastiera'),
        ('bassista','Bassista'),
        ('percussioni','Percussioni'),
        ('batteria','Batteria')]
    )

    class Meta:
        model = PrenotaEvento
        fields = ['nome_cliente','cognome_cliente','email','citta','provincia','telefono','tipo_evento','luogo','citta_evento','prov_evento','indirizzo_evento','data_evento','seleziona_artista','captcha'  ]
    
    
    def __init__(self, *args, **kwargs):
        super(PrenotaEventiForm, self).__init__(*args, **kwargs)
        self.fields['nome_cliente'].widget.attrs.update({'class':'form-control input_elem', 'required':True,'autocomplete': 'nome_contatto', 'placeholder':'Nome*'})
        self.fields['cognome_cliente'].widget.attrs.update({'class':'form-control input_elem', 'required':True,'autocomplete': 'cognome_contatto', 'placeholder':'Cognome*'})
        self.fields['email'].widget.attrs.update({'class':'form-control input_elem', 'pattern':"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$",'required':False,'autocomplete': 'email', 'placeholder':'Email'})
        self.fields['citta'].widget.attrs.update({'class':'form-control input_elem', 'required':True,'autocomplete': 'citta_contatto', 'placeholder':'Città*'})
        self.fields['provincia'].widget.attrs.update({'class':'form-control input_elem', 'pattern':"^[a-zA-Z]{2}$", 'required':True,'autocomplete': 'provincia_contatto', 'placeholder':'Sigla della provincia*'})
        self.fields['telefono'].widget.attrs.update({'class':'form-control input_elem', 'required':True,'autocomplete': 'cellulare_contatto', 'placeholder':'Cellulare*'})
        self.fields['tipo_evento'].widget.attrs.update({'class':'form-control input_elem', 'required':True,'autocomplete': 'tipo_evento', 'placeholder':'Tipo di evento (matrimonio, compleanno,...)*'})
        self.fields['luogo'].widget.attrs.update({'class':'form-control input_elem', 'required':False,'autocomplete': 'luogo_evento', 'placeholder':'Nome della sala o del luogo privato'})
        self.fields['citta_evento'].widget.attrs.update({'class':'form-control input_elem', 'required':True,'autocomplete': 'citta_evento', 'placeholder':'Città*'})
        self.fields['prov_evento'].widget.attrs.update({'class':'form-control input_elem', 'pattern':"^[a-zA-Z]{2}$", 'required':True,'autocomplete': 'provincia_evento', 'placeholder':'Sigla della provincia*'})
        self.fields['indirizzo_evento'].widget.attrs.update({'class':'form-control input_elem', 'required':False,'autocomplete': 'indirizzo_evento', 'placeholder':'Via/Piazza e numero civico'})
        self.fields['data_evento'].widget.attrs.update({'class':'form-group col-md-6', 'required':True, 'placeholder':'gg/mm/aaaa*'})
        # self.fields['seleziona_artisti'].widget.attrs.update({'size':3,'class':'form-group col-md-6', 'required':True, 'placeholder':'Partecipanti della band all\'evento*'})


        