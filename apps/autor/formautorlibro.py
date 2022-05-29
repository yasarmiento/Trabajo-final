from apps.autor.models import Autorlibro
from django import forms


class Autorlibroform(forms.ModelForm):
    class Meta:
        model= Autorlibro
        
        fields = {
            'autorid',
            'libroid',
        }
        
        labels = {
            'autorid': 'Seleccione el autor',
            'libroid': 'Seleccione el libro',
        }
        
        widgets = {
            'autorid': forms.Select(attrs= {'class': 'form-control'}),
            'libroid': forms.Select(attrs= {'class': 'form-control'}),  
        }