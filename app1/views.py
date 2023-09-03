from django.shortcuts import render, redirect
from .models import Curso, Profesor, Estudiante, Fechaproxima, Avatar
from .forms import CursoForm, Profesorform, Estudianteform, Fechasform, RegistroUsuariosForm, UEditForm, AvatarFormulario
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth       import authenticate, login


from django.contrib.auth.decorators import login_required



# Create your views here.

#----------------------------------->Main pages

def home (request):
    return render(request, "aplicacion/home.html")

@login_required
def cursos (request):
    contexto = {"cursos": Curso.objects.all(), 'titulo': 'Cursos disponibles', 'comisiones':['comision 1', 'comision 2', 'comision 3']}
    return render(request, "aplicacion/cursos.html", contexto)

@login_required
def profesores (request):
    contexto = {"profesores": Profesor.objects.all(), 'titulo': 'Profesores disponibles'}
    return render(request, "aplicacion/profesores.html", contexto)

@login_required
def estudiantes (request):
    contexto = {"estudiantes": Estudiante.objects.all(), 'titulo': 'Estudiantes disponibles'}
    return render(request, "aplicacion/estudiantes.html", contexto)

@login_required
def fechaproxima (request):
    contexto = {"fechasproximas": Fechaproxima.objects.all(), 'titulo': 'Proximas fechas disponibles'}
    return render(request, "aplicacion/fechaproxima_list.html", contexto)



#-----------------------------------> Forms
@login_required
def cursoform(request):
    if request.method == "POST":
        curso = Curso(nombre=request.POST['nombre'],
                      comision=request.POST['comision'])
        curso.save()
        return HttpResponse("Nueva asignatura/curso agregada con exito!")
    
    return render(request, "aplicacion/cursoform.html")

@login_required
def cursoform2(request):
    if request.method == "POST":
        miform= CursoForm(request.POST)
        if miform.is_valid():
            name_curso= miform.cleaned_data.get('nombre')
            name_comision= miform.cleaned_data.get('comision')
            curso= Curso(nombre = name_curso,
                         comision= name_comision)
            curso.save()
            return render(request, "aplicacion/base.html")
    else:
        miform= CursoForm()
    return render (request, "aplicacion/cursoform2.html", {"form": miform})


@login_required
def searchcomision(request):
    return render (request, "aplicacion/searchcomision.html")

@login_required
def search2(request):
    if request.GET['buscar']:
        patron= request.GET['buscar']
        cursos= Curso.objects.filter(nombre__icontains=patron)
        contexto= {"cursos": cursos, "titulo":f"Busqueda en funcion del caracter '{patron}'"}
        return render(request, "aplicacion/cursos.html", contexto)
    
    return HttpResponse ("Vuelva a intentarlo, ingreso invalido, asegurate de llenar todos los campos")

@login_required
def profesorform(request):
    if request.method == "POST":
        miform= Profesorform (request.POST)
        if miform.is_valid():
            name_nombre= miform.cleaned_data.get('nombre')
            name_apellido= miform.cleaned_data.get('apellido')
            name_email= miform.cleaned_data.get('email')
            name_profesion= miform.cleaned_data.get('profesion')
            profesor= Profesor(nombre = name_nombre,
                         apellido= name_apellido,
                         email= name_email,
                         profesion= name_profesion)
            profesor.save()
            return render(request, "aplicacion/base.html")
    else:
        miform= Profesorform()
    return render (request, "aplicacion/profesorform.html", {"form": miform})

@login_required
def searchprofesor(request):
    return render (request, "aplicacion/searchprofesor.html")

@login_required
def searchprofesor2(request):
    if request.GET['buscar']:
        patron= request.GET['buscar']
        profesores= Profesor.objects.filter(nombre__icontains= patron)
        contexto= {"profesores": profesores}
        return render(request, "aplicacion/profesores.html", contexto)
    
    return HttpResponse ("Vuelva a intentarlo, ingreso invalido, asegurate de llenar todos los campos")


@login_required
def estudiantesform(request):
    if request.method == "POST":
        miform=  Estudianteform(request.POST)
        if miform.is_valid():
            name_nombre= miform.cleaned_data.get('nombre')
            name_apellido= miform.cleaned_data.get('apellido')
            name_email= miform.cleaned_data.get('email')
            
            estudiante= Estudiante(nombre = name_nombre,
                         apellido= name_apellido,
                         email= name_email,
            )
            estudiante.save()
            return render(request, "aplicacion/base.html")
    else:
        miform= Estudianteform()
    return render (request, "aplicacion/estudianteform.html", {"form": miform})

@login_required
def searchestudiante(request):
    return render (request, "aplicacion/searchestudiante.html")

@login_required
def searchestudiante2(request):
    if request.GET['buscar']:
        patron= request.GET['buscar']
        estudiantes= Estudiante.objects.filter(nombre__icontains= patron)
        contexto= {"estudiantes": estudiantes}
        return render(request, "aplicacion/estudiantes.html", contexto)
    
    return HttpResponse ("Vuelva a intentarlo, ingreso invalido, asegurate de llenar todos los campos")

#-----------------------------------------------------> CRUD


        #----------------------------------------> model profesores

@login_required
def updprofesor (request, id_profe ):
    profesor= Profesor.objects.get (id = id_profe)
    if request.method == "POST" :
        miForm = Profesorform(request.POST)
        if miForm.is_valid():
            profesor.nombre = miForm.cleaned_data.get('nombre')
            profesor.apellido = miForm.cleaned_data.get('apellido')
            profesor.email = miForm.cleaned_data.get('email')
            profesor.profesion = miForm.cleaned_data.get('profesion')
            profesor.save()
            return redirect(reverse_lazy('profesores'))
    else:
        miForm = Profesorform (initial = {

            'nombre' : profesor.nombre,
            'apellido' : profesor.apellido,
            'email' : profesor.email,
            'profesion' : profesor.profesion,

        })

    return render (request, "aplicacion/profesorform.html", {'form' : miForm})

@login_required
def delProfesor (request, id_profe):
    profesor = Profesor.objects.get(id=id_profe)
    profesor.delete()
    return redirect(reverse_lazy('profesores'))


@login_required
def buildprofesor(request):    
    if request.method == "POST":
        miForm = Profesorform(request.POST)
        if miForm.is_valid():
            p_nombre = miForm.cleaned_data.get('nombre')
            p_apellido = miForm.cleaned_data.get('apellido')
            p_email = miForm.cleaned_data.get('email')
            p_profesion = miForm.cleaned_data.get('profesion')
            profesor = Profesor(nombre=p_nombre, 
                              apellido=p_apellido,
                             email=p_email,
                             profesion=p_profesion,
                             )
            profesor.save()
            return redirect(reverse_lazy('profesores'))
    else:
        miForm = Profesorform()

    return render(request, "aplicacion/profesorform.html", {"form":miForm})

        #----------------------------------------------> model cursos

@login_required
def updcurso (request, id_curso ):
    curso = Curso.objects.get (id = id_curso)
    if request.method == "POST" :
        miForm = CursoForm(request.POST)
        if miForm.is_valid():
            curso.nombre = miForm.cleaned_data.get('nombre')
            curso.comision = miForm.cleaned_data.get('comision')
            curso.save()
            return redirect(reverse_lazy('cursos'))
    else:
        miForm = CursoForm (initial = {

            'nombre' : curso.nombre,
            'comision' : curso.comision,
            

        })

    return render (request, "aplicacion/cursoform2.html", {'form' : miForm})


@login_required
def delcurso (request, id_curso):
    curso = Curso.objects.get(id=id_curso)
    curso.delete()
    return redirect(reverse_lazy('cursos'))


@login_required
def buildcurso(request):    
    if request.method == "POST":
        miForm = CursoForm(request.POST)
        if miForm.is_valid():
            c_nombre = miForm.cleaned_data.get('nombre')
            c_comision = miForm.cleaned_data.get('comision')
            
            curso = Curso(nombre=c_nombre, 
                              comision=c_comision,
                             
                             )
            curso.save()
            return redirect(reverse_lazy('cursos'))
    else:
        miForm = CursoForm()

    return render(request, "aplicacion/cursoform2.html", {"form":miForm})


        #------------------------------------------------> model Estudiante 

@login_required
def updestudiante (request, id_estudiante ):
    estudiante = Estudiante.objects.get (id = id_estudiante)
    if request.method == "POST" :
        miForm = Estudianteform(request.POST)
        if miForm.is_valid():
            estudiante.nombre = miForm.cleaned_data.get('nombre')
            estudiante.apellido = miForm.cleaned_data.get('apellido')
            estudiante.email = miForm.cleaned_data.get('email')
            estudiante.save()
            return redirect(reverse_lazy('estudiantes'))
    else:
        miForm = Estudianteform (initial = {

            'nombre' : estudiante.nombre,
            'apellido' : estudiante.apellido,
            'email' : estudiante.email,
            

        })

    return render (request, "aplicacion/estudianteform.html", {'form' : miForm})


@login_required
def delestudiante (request, id_estudiante):
    estudiante = Estudiante.objects.get(id=id_estudiante)
    estudiante.delete()
    return redirect(reverse_lazy('estudiantes'))


@login_required
def buildestudiante(request):    
    if request.method == "POST":
        miForm = Estudianteform(request.POST)
        if miForm.is_valid():
            e_nombre = miForm.cleaned_data.get('nombre')
            e_apellido = miForm.cleaned_data.get('apellido')
            e_email = miForm.cleaned_data.get('email')
            
            estudiante = Estudiante(nombre=e_nombre, 
                              apellido=e_apellido,
                              email=e_email,
                             
                             )
            estudiante.save()
            return redirect(reverse_lazy('estudiantes'))
    else:
        miForm = Estudianteform()

    return render(request, "aplicacion/estudianteform.html", {"form":miForm})

        #----------------------------------------------> model proximas fechas

@login_required
def updfechaproxima (request, id_fechaproxima ):
    proximafecha = Fechaproxima.objects.get (id = id_fechaproxima)
    if request.method == "POST" :
        miForm = Fechasform(request.POST)
        if miForm.is_valid():
            proximafecha.nombre = miForm.cleaned_data.get('nombre')
            proximafecha.fechaProxima = miForm.cleaned_data.get('fechaProxima')
            
            proximafecha.save()
            return redirect(reverse_lazy('fechas_proximas'))
    else:
        miForm = Fechasform (initial = {

            'nombre' : proximafecha.nombre,
            'fechaProxima' : proximafecha.fechaProxima,
            
            

        })

    return render (request, "aplicacion/fechaproximaform.html", {'form' : miForm})


@login_required
def delfechaproxima (request, id_fechaproxima):
    fecha = Fechaproxima.objects.get(id=id_fechaproxima)
    fecha.delete()
    return redirect(reverse_lazy('fechas_proximas'))


@login_required
def buildfechaproxima(request):    
    if request.method == "POST":
        miForm = Fechasform(request.POST)
        if miForm.is_valid():
            f_nombre = miForm.cleaned_data.get('nombre')
            f_fechaproxima = miForm.cleaned_data.get('fechaProxima')
            
            fechaproxima = Fechaproxima (nombre = f_nombre, 
                              fechaProxima = f_fechaproxima,
                             
                             )
            fechaproxima.save()
            return redirect(reverse_lazy('fechas_proximas'))
    else:
        miForm = Fechasform()

    return render(request, "aplicacion/fechaproximaform.html", {"form":miForm})


#---------------------------------------------------> Login / logout / registracion

def loginrequest(request):
     if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)

                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.jpg"
                finally:
                    request.session["avatar"] = avatar

                return render(request, "aplicacion/base.html", {'mensaje': f'Acceso exitoso, bienvenido {usuario}'})
            else:
                return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Datos invalidos, intente nuevamente'})
        else:
            return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Datos invalidos, intente nuevamente'})

     miForm =   AuthenticationForm()      

     return render(request, "aplicacion/login.html", {"form":miForm})  


def registrou(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm =   RegistroUsuariosForm()      
    return render(request, "aplicacion/registro.html", {"form":miForm}) 

@login_required
def editPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request,"aplicacion/base.html")
        else:
            return render(request,"aplicacion/editPerfil.html", {'form': form, 'usuario': usuario.username})
    else:
        form = UEditForm(instance=usuario)
    return render(request, "aplicacion/editPerfil.html", {'form': form, 'usuario': usuario.username})


@login_required
def aggAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES) # Diferente a los forms tradicionales
        if form.is_valid():
            u = User.objects.get(username=request.user)

            # ____ Para borrar el avatar viejo
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            # ____ Guardar el nuevo
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # ___ Hago que la url de la imagen viaje en el request
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"aplicacion/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/aggAvatar.html", {'form': form })