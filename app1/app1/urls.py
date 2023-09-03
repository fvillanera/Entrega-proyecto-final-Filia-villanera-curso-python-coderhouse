from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
#--------------------------------> Rutas Main pages
    path('', home, name="home" ),
    path('cursos/', cursos, name="cursos" ),
    path('profesores/', profesores, name="profesores" ),
    path('estudiantes/', estudiantes, name="estudiantes" ),
    path('fechas_proximas/', fechaproxima , name= "fechas_proximas" ),
    
#--------------------------------> Rutas Formularios
    path('curso_form/', cursoform, name="curso_form" ),
    path('curso_form2/', cursoform2, name="curso_form2" ),#agregar guardar curso

    path('buscar_comision/',searchcomision, name="buscar_comision" ),#buscar curso
    path('buscar2/', search2, name="buscar2" ),

    path('profesorform/', profesorform, name="profesorform" ),#agregar/guardar profesor
    path('search_profesor/',searchprofesor, name="search_profesor" ),#buscar profesor
    path('buscar3/', searchprofesor2, name="buscar3" ),

    path('estudianteform/', estudiantesform, name="estudianteform" ),#agregar estudiante
    path('searchestudiante/', searchestudiante, name="searchestudiante" ),
    path('buscar4/', searchestudiante2, name="buscar4" ),

#--------------------------------------> CRUD

    path('upd_curso/<id_curso>/', updcurso, name="upd_curso" ),  
    path('del_curso/<id_curso>/', delcurso, name="del_curso" ), 
    path('build_curso/', buildcurso, name="build_curso" ),
    

    path('upd_profesor/<id_profe>/', updprofesor, name="upd_profesor" ),    
    path('del_profesor/<id_profe>/', delProfesor, name="del_profesor" ),  
    path('build_profesor/', buildprofesor, name="build_profesor" ),


    path('upd_estudiante/<id_estudiante>/', updestudiante, name="upd_estudiante" ),  
    path('del_estudiante/<id_estudiante>/', delestudiante, name="del_estudiante" ), 
    path('build_estudiante/', buildestudiante, name="build_estudiante" ),

   
   
    path('upd_fechaproxima/<id_fechaproxima>/', updfechaproxima, name="upd_fechaproxima" ),    
    path('del_fechaproxima/<id_fechaproxima>/', delfechaproxima, name="del_fechaproxima" ),  
    path('build_fechaproxima/', buildfechaproxima, name="build_fechaproxima" ),

    path('login/', loginrequest, name="login" ),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout" ),
    path('registro/', registrou, name="registro" ),
    path('editarperfil/', editPerfil, name="editarperfil" ),
    path('agg_avatar/', aggAvatar, name="agg_avatar" ),



]