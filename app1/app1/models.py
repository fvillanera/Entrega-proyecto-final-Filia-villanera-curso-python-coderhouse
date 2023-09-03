from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

# Create your models here.

class Curso (LoginRequiredMixin, models.Model):
    nombre = models.CharField(max_length=50)
    comision  = models.IntegerField()
    def __str__ (self):
        return f"{self.nombre} / Comision: {self.comision}"
    
class Estudiante (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__ (self):
        return f"{self.nombre}, {self.apellido}"
    
class Profesor(LoginRequiredMixin, models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    def __str__ (self):
        return f"{self.nombre}, {self.apellido}"
    
    class Meta:
        verbose_name = "profesor"
        verbose_name_plural = "profesores"
        ordering = ["apellido"]
    

class Fechaproxima (LoginRequiredMixin, models.Model):
    nombre = models.CharField(max_length=50)
    fechaProxima = models.DateField()
    
    def __str__(self):
        return f"{self.nombre}, {self.fechaProxima}"
    class Meta:
        verbose_name = "fecha proxima"
        verbose_name_plural = "fechas proximas"


class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"

    