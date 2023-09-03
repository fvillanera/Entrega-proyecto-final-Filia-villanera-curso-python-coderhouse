from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

class CursoForm (LoginRequiredMixin, forms.Form):
    nombre= forms.CharField(max_length=50, required=True)
    comision= forms.IntegerField(required=True)
    

class Profesorform (LoginRequiredMixin, forms.Form):
     nombre= forms.CharField(label = "Nombre", max_length=50, required=True)
     apellido= forms.CharField(label = "Apellido", max_length=50, required=True)
     email= forms.EmailField(required=True)
     profesion= forms.CharField(label = "Profesion", max_length=50, required=True)

class Estudianteform (LoginRequiredMixin, forms.Form):
     nombre= forms.CharField(max_length=50, required=True)
     apellido= forms.CharField(max_length=50, required=True)
     email= forms.EmailField(required=True)

class Fechasform (LoginRequiredMixin, forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length=50, required=True )
    fechaProxima = forms.DateField(label = "Fecha (AAAA-MM-DD)", required=True)

class RegistroUsuariosForm(UserCreationForm):    
    email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UEditForm(UserCreationForm):
    email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(label="Clave", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Clave", widget= forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)   
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)   

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']


class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)

     