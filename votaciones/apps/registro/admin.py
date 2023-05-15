from django.contrib import admin
from .models import *
# Register your models here.


class GeneroAdmin(admin.ModelAdmin):
    search_fields = ['item_genero']
    list_display = ('item_genero', 'estado', 'fecha_creacion', )


class LocalidadAdmin(admin.ModelAdmin):
    search_fields = ['nombre_localidad']
    list_display = ('nombre_localidad', 'estado', 'fecha_creacion', )


class TipoDocumentoAdmin(admin.ModelAdmin):
    search_fields = ['nombre_tipo_documento']
    list_display = ('nombre_tipo_documento', 'estado', 'fecha_creacion', )


class VotanteAdmin(admin.ModelAdmin):
    search_fields = ['no_documento_votante']
    list_display = ('no_documento_votante', 'nombres_votante',
                    'apellidos_votante', 'estado', 'fecha_creacion', )


class CandidatoAdmin(admin.ModelAdmin):
    search_fields = ['no_documento_candidato']
    list_display = ('no_documento_candidato', 'nombres_candidato',
                    'apellidos_candidato',   'partido_candidato', 'estado', 'fecha_creacion', )


admin.site.register(Genero, GeneroAdmin)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(TipoDocumento, TipoDocumentoAdmin)
admin.site.register(Votante, VotanteAdmin)
admin.site.register(Candidato, CandidatoAdmin)
