from django.shortcuts import render, redirect
from apps.registro.models import *
from .models import Voto
from django.contrib import messages

# Create your views here.


def votarHome(request):
    candidato = Candidato.objects.filter(estado=True)
    template_name = 'votar/votar.html'
    contexto = {
        'candidato': candidato,

    }

    return render(request, template_name, contexto)


def registrarVoto(request):
    noDocumentoVotante = request.POST['txtNoDocumentoVotante']
    tipoDocumentoCandidato = request.POST.getlist('select-candidato')

    votante = Votante.objects.filter(no_documento_votante=noDocumentoVotante)
    candidato = Candidato.objects.filter(
        no_documento_candidato=tipoDocumentoCandidato[0])

    voto = Voto.objects.filter(no_documento_votante=noDocumentoVotante)

    print(voto)
    if len(voto) > 0:
        messages.success(request, 'No se puede realizar dos votos')
    else:
        if votante:
            if candidato:
                if votante[0].id_localidad_votante == candidato[0].id_localidad_candidato:
                    Voto.objects.create(no_documento_votante=noDocumentoVotante,
                                        no_documento_candidato=tipoDocumentoCandidato[0]
                                        )
                    messages.success(
                        request, 'Se realizo el voto correctamente')
                else:
                    messages.success(
                        request, 'El votante pertenece a otra localidad que el candidato')
            else:
                messages.success(
                    request, 'El candidato no se encuentra registrado')
        else:
            messages.success(request, 'El votante no se encuentra registrado')

    return redirect('/votar')
