from apps.autor.models import Libro
from django import forms


class Libroform(forms.ModelForm):
    class Meta:
        model= Libro
        
        fields = {
            'titulo',
            'numeropagina',
            'editor',
            'isbn',
            'ejemplaresid',
        }
        
        labels = {
            'titulo': 'Ingresar el titulo',
            'numeropagina': 'ingrese la cantidad de paginas',
            'editor': 'ingrese al editor',
            'isbn': 'ingrese el ISBN',
            'ejemplaresid': 'Seleccione el ejemplar',
        }
        
        widgets = {
            'titulo': forms.TextInput(attrs= {'class': 'form-control'}),
            'numeropagina': forms.TextInput(attrs= {'class': 'form-control'}),
            'editor': forms.TextInput(attrs= {'class': 'form-control'}),
            'isbn': forms.TextInput(attrs= {'class': 'form-control'}),
            'ejemplaresid': forms.Select(attrs= {'class': 'form-control'}), 
        }