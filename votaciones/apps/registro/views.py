from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.


def votanteHome(request):
    template_name = 'registro/gestionVotante.html'
    genero = Genero.objects.filter(estado=True)
    tipoDocumento = TipoDocumento.objects.filter(estado=True)
    localidad = Localidad.objects.filter(estado=True)
    infoVotantes = Votante.objects.filter(estado=True)

    contexto = {
        'genero': genero,
        'tipoDocumento': tipoDocumento,
        'localidad': localidad,
        'votante': infoVotantes,
    }

    return render(request, template_name, contexto)


def candidatoHome(request):
    template_name = 'registro/gestionCandidato.html'
    genero = Genero.objects.filter(estado=True)
    tipoDocumento = TipoDocumento.objects.filter(estado=True)
    localidad = Localidad.objects.filter(estado=True)
    infoCandidato = Candidato.objects.filter(estado=True)
    candidatoItem = True

    contexto = {
        'genero': genero,
        'tipoDocumento': tipoDocumento,
        'localidad': localidad,
        'candidato': infoCandidato,
        'candidatoItem': candidatoItem,
    }

    return render(request, template_name, contexto)


def registrarVotante(request):
    noDocumento = request.POST['txtNoDocumento']
    tipoDocumento = request.POST.getlist('select-tipo-documento')
    nombres = request.POST['txtNombre']
    apellidos = request.POST['txtApellidos']
    genero = request.POST.getlist('select-genero')
    localidad = request.POST.getlist('select-localidad')

    Votante.objects.create(no_documento_votante=noDocumento,
                           id_tipo_documento_id=int(tipoDocumento[0]),
                           nombres_votante=nombres,
                           apellidos_votante=apellidos,
                           id_genero_votante_id=int(genero[0]),
                           id_localidad_votante_id=int(localidad[0]))
    messages.success(request, 'Votante Registrado')
    return redirect('/')


def registrarCandidato(request):
    noDocumento = request.POST['txtNoDocumento']
    tipoDocumento = request.POST.getlist('select-tipo-documento')
    nombres = request.POST['txtNombre']
    apellidos = request.POST['txtApellidos']
    partido = request.POST['txtPartido']
    genero = request.POST.getlist('select-genero')
    localidad = request.POST.getlist('select-localidad')

    Candidato.objects.create(no_documento_candidato=noDocumento,
                             id_tipo_documento_id=int(tipoDocumento[0]),
                             nombres_candidato=nombres,
                             apellidos_candidato=apellidos,
                             partido_candidato=partido,
                             id_genero_candidato_id=int(genero[0]),
                             id_localidad_candidato_id=int(localidad[0]))

    messages.success(request, 'Candidato Registrado')
    return redirect('/candidato/')


def eliminarVotante(request, codigo_votante):
    votante = Votante.objects.get(no_documento_votante=codigo_votante)
    votante.delete()

    messages.success(request, 'Votante Eliminado')
    return redirect('/')


def eliminarCandidato(request, codigo_candidato):
    print(codigo_candidato)
    candidato = Candidato.objects.get(no_documento_candidato=codigo_candidato)
    candidato.delete()

    messages.success(request, 'Candidato Eliminado')
    return redirect('/candidato/')
