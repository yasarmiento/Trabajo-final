from django.db import models
from apps.usuario.models import Ejemplares

# Create your models here.

class Autor (models.Model):
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre
    
class Libro (models.Model):
    titulo = models.CharField(max_length=50)
    numeropagina = models.CharField(max_length=20)
    editor = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    ejemplaresid = models.ForeignKey(Ejemplares, on_delete=models.CASCADE)
    autorid = models.ManyToManyField(Autor, through='Autorlibro')
    
    
class Autorlibro (models.Model):
    autorid = models.ForeignKey(Autor, on_delete=models.CASCADE)
    libroid = models.ForeignKey(Libro, on_delete=models.CASCADE)