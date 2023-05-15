from django.db import models

# Create your models here.


class Voto(models.Model):
    """Model definition for Voto."""
    id_voto = models.AutoField(primary_key=True)
    no_documento_votante = models.CharField('No documento votante', max_length=50,
                                            null=False, blank=False)
    no_documento_candidato = models.CharField('No documento votante', max_length=50,
                                              null=False, blank=False)
    estado = models.BooleanField('Localidad Activo/Inactivo', default=True)
    fecha_creacion = models.DateField(
        'Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        """Meta definition for Localidad."""

        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidads'
        ordering = ['id_voto']

    def __str__(self):
        """Unicode representation of Localidad."""
        return self.no_documento_votante
