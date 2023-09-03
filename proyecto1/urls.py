
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from proyecto1 import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', bienvenida ),
    path('welcome2/', bienvenida_html ),
    path('welcome3/', bienvenida_template ),
    path('comision_1/', comision_1 ),
    path('agregar_curso/', agg_curso ),

    path('saludar/<nombre>/', saludar ),
    path('tpropina/<total>/', total_propina  ),
    path('saludar2/<nombre>/<apellido>/', saludar2 ),
    path('', include('app1.urls') ),
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
