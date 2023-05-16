from django.contrib import admin
from .models import *

# Register your models here.


class VotarAdmin(admin.ModelAdmin):
    search_fields = ['no_documento_votante']
    list_display = ('no_documento_votante',
                    'no_documento_candidato', 'estado', 'fecha_creacion', )


admin.site.register(Voto, VotarAdmin)
