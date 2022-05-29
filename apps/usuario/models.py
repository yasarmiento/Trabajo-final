from django.db import models

# Create your models her

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=30)
    direccion = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre
    
class Ejemplares (models.Model):
    codigolibro = models.CharField(max_length=20)
    localizacion = models.CharField(max_length=20)
    usuarioid = models.ManyToManyField(Usuario, through='Prestar')
    
    def __str__(self):
        return self.codigolibro
    
class Prestar (models.Model):
    fechadev = models.CharField(max_length=20)
    fechapres = models.CharField(max_length=20)
    usuarioid = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ejemplaresid = models.ForeignKey(Ejemplares, on_delete=models.CASCADE)
    