from django.urls import path, include
from .views import *

urlpatterns = [
   
    path('',home, name='home' ),
    path('db/',db, name='db' ),
    path('pedidoForm/',pedidoForm, name='pedidoForm' ),
    path('registroForm/',registroForm, name='registroForm' ),
    path('aplicanteForm/',aplicanteForm, name='aplicanteForm' ),
    path('libroForm/',libroForm, name='libroForm' ),
    path('buscarLibro/',buscarLibro, name='buscarLibro' ),
    path('buscar/',buscar, name='buscar' ),
    
]