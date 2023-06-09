from django.db import models

# Create your models here.

class Denuncia(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)    
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre