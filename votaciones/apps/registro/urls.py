from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', votanteHome, name='votante'),
    path('candidato/', candidatoHome, name='candidato'),
    path('registrarVotante/', registrarVotante, name='registrarVotante'),
    path('registrarCandidato/', registrarCandidato, name='registrarCandidato'),
    path('eliminarVotante/<codigo_votante>',
         views.eliminarVotante, name='eliminarVotante'),
    path('candidato/eliminarCandidato/<codigo_candidato>',
         views.eliminarCandidato, name="eliminarCandidato"),

]
