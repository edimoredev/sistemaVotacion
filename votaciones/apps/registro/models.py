from django.db import models

# Create your models here.


class Genero(models.Model):
    """Model definition for Genero."""
    id_genero = models.PositiveBigIntegerField(primary_key=True)
    item_genero = models.CharField('Item Genero', max_length=20,
                                   null=False, blank=False)
    estado = models.BooleanField('Genero Activo/Inactivo', default=True)
    fecha_creacion = models.DateField(
        'Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        """Meta definition for Genero."""

        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'
        ordering = ['item_genero']

    def __str__(self):
        """Unicode representation of Genero."""
        return self.item_genero


class Localidad(models.Model):
    """Model definition for Localidad."""
    id_localidad = models.AutoField(primary_key=True)
    nombre_localidad = models.CharField('Nombre Localidad', max_length=50,
                                        null=False, blank=False)
    estado = models.BooleanField('Localidad Activo/Inactivo', default=True)
    fecha_creacion = models.DateField(
        'Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        """Meta definition for Localidad."""

        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidads'
        ordering = ['nombre_localidad']

    def __str__(self):
        """Unicode representation of Localidad."""
        return self.nombre_localidad


class TipoDocumento(models.Model):
    """Model definition for TipoDocumento."""
    id_tipo_documento = models.AutoField(primary_key=True)
    nombre_tipo_documento = models.CharField('Nombre Tipo documnento', max_length=50,
                                             null=False, blank=False)
    estado = models.BooleanField(
        'Tipo Documento Activo/Inactivo', default=True)
    fecha_creacion = models.DateField(
        'Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        """Meta definition for Localidad."""

        verbose_name = 'TipoDocumento'
        verbose_name_plural = 'TipoDocumento'
        ordering = ['nombre_tipo_documento']

    def __str__(self):
        """Unicode representation of Localidad."""
        return self.nombre_tipo_documento


class Votante(models.Model):
    """Model definition for Votante."""

    no_documento_votante = models.CharField('Numero documento', primary_key=True, max_length=20,
                                            null=False, blank=False)

    nombres_votante = models.CharField('Nombres', null=False, blank=False)
    apellidos_votante = models.CharField('Apellidos', null=False, blank=False)
    id_tipo_documento = models.ForeignKey(
        TipoDocumento, on_delete=models.CASCADE, null=False, blank=False)
    id_genero_votante = models.ForeignKey(
        Genero, on_delete=models.CASCADE, null=False, blank=False)
    id_localidad_votante = models.ForeignKey(
        Localidad, on_delete=models.CASCADE, null=False, blank=False)

    estado = models.BooleanField('Votante Activo/Inactivo', default=True)
    fecha_creacion = models.DateField(
        'Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        """Meta definition for Votante."""

        verbose_name = 'Votante'
        verbose_name_plural = 'Votantes'
        ordering = ['nombres_votante']

    def __str__(self):
        """Unicode representation of Votante."""
        return self.nombres_votante


class Candidato(models.Model):
    """Model definition for Candidato."""

    no_documento_candidato = models.CharField('Numero documento', primary_key=True, max_length=20,
                                              null=False, blank=False)

    nombres_candidato = models.CharField('Nombres', null=False, blank=False)
    apellidos_candidato = models.CharField(
        'Apellidos', null=False, blank=False)
    id_tipo_documento = models.ForeignKey(
        TipoDocumento, on_delete=models.CASCADE, null=False, blank=False)
    partido_candidato = models.CharField(
        'Partido candidato', null=False, blank=False)
    id_genero_candidato = models.ForeignKey(
        Genero, on_delete=models.CASCADE, null=False, blank=False)
    id_localidad_candidato = models.ForeignKey(
        Localidad, on_delete=models.CASCADE, null=False, blank=False)
    estado = models.BooleanField('Votante Activo/Inactivo', default=True)
    fecha_creacion = models.DateField(
        'Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        """Meta definition for Votante."""

        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'
        ordering = ['nombres_candidato']

    def __str__(self):
        """Unicode representation of Candidato."""
        return self.nombres_candidato
