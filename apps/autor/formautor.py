from django import forms
from apps.autor.models import Autor

class Autorform(forms.ModelForm):
    class Meta:
        model= Autor
        
        fields = {
            'nombre',
        }
        
        labels = {
            'nombre': 'Ingresar su nombre',
        }
        
        widgets = {
            'nombre': forms.TextInput(attrs= {'class': 'form-control'}),
        }