from apps.usuario.models import Ejemplares
from django import forms

class Ejemplaresform(forms.ModelForm):
    class Meta:
        model= Ejemplares
        
        fields = {
            'codigolibro',
            'localizacion',
        }
        
        labels = {
            'codigolibro': 'Ingresar el codigo del libro',
            'localizacion': 'Ingrese la ubicacion del libro',
        }
        
        widgets = {
            'codigolibro': forms.TextInput(attrs= {'class': 'form-control'}),
            'localizacion': forms.TextInput(attrs= {'class': 'form-control'}),
        }