from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('votar/', votarHome, name='votante'),
    path('registrarVoto/', registrarVoto, name='registrarVoto'),
]
