from apps.usuario.models import Prestar
from django import forms


class Prestarform(forms.ModelForm):
    class Meta:
        model= Prestar
        
        fields = {
            'fechadev',
            'fechapres',
            'usuarioid',
            'ejemplaresid',
        }
        
        labels = {
            'fechadev': 'Ingresar la fecha de devolucion',
            'fechapres': 'Ingrese  la fecha de prestamo',
            'usuarioid': 'Seleccione su usuario',
            'ejemplaresid': 'Seleccione el ejemplar',
        }
        
        widgets = {
            'fechadev': forms.TextInput(attrs= {'class': 'form-control'}),
            'fechapres': forms.TextInput(attrs= {'class': 'form-control'}),
            'usuarioid': forms.Select(attrs= {'class': 'form-control'}),
            'ejemplaresid': forms.Select(attrs= {'class': 'form-control'}),  
        }