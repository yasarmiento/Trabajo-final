from django import forms
from apps.usuario.models import Usuario

class Usuarioform(forms.ModelForm):
    class Meta:
        model= Usuario
        
        fields = {
            'nombre',
            'apellidos',
            'direccion',
            'telefono',
        }
        
        labels = {
            'nombre': 'Ingresar su nombre',
            'apellidos': 'Ingrese sus apellidos',
            'direccion': 'Ingrese su direccion',
            'telefono': 'Ingrese su telefono',
        }
        
        widgets = {
            'nombre': forms.TextInput(attrs= {'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs= {'class': 'form-control'}),
            'direccion': forms.TextInput(attrs= {'class': 'form-control'}),
            'telefono': forms.TextInput(attrs= {'class': 'form-control'}),  
        }