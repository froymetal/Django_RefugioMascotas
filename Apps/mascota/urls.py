from django.urls import path
from django.conf.urls import url,include
from Apps.mascota.views import index,mascota_view,prueba, listar_mascota

urlpatterns = [
    #cadenavacia
    #url(r'^$', index),
    #path('',index),
    #url(r'^$',index, name='index'),
    #url(r'^nuevo$',mascota_view, name='mascota_crear'),
    
    #path('',prueba, name='mascotaprueba'),
    path('',mascota_view, name='mascotaform'),
    path('crear_mascota/',prueba, name='crear_mascota'),
    path('listar_mascota/',listar_mascota, name='listar_mascota'),
]