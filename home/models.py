from django.db import models


class AreaCoordinacion(models.Model):
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "area_coordinacion"

    nombre = models.CharField(max_length=100)
    estatus = models.BooleanField(default=True)

    def get_personas(self):
        return PersonaCoordinacion.objects.filter(
            area_coordinacion=self,
            estatus=True,
        )


class PersonaCoordinacion(models.Model):
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "persona_coordinacion"

    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100, null=True)
    extension = models.CharField(max_length=10, null=True)
    correo = models.EmailField(max_length=100)
    estatus = models.BooleanField(default=True)
    imagen = models.CharField(max_length=100, null=True)
    area_coordinacion = models.ForeignKey(
        AreaCoordinacion,
        on_delete=models.CASCADE,
        related_name="personas",
    )


class PersonaColegio(models.Model):
    def __str__(self):
        return self.estado

    class Meta:
        db_table = "persona_colegio"

    estado = models.CharField(max_length=100)
    director_general = models.CharField(max_length=100)
    direccion = models.TextField(max_length=200, null=True)
    telefono = models.CharField(max_length=50, null=True)
    estatus = models.BooleanField(default=True)


class MisionYVision(models.Model):
    class Meta:
        db_table = "mision_y_vision"

    mision = models.TextField(max_length=500)
    vision = models.TextField(max_length=500)
    estatus = models.BooleanField(default=True)


class OfertaEducativaArea(models.Model):
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "oferta_educativa_area"

    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField(default=True)

    def get_carreras(self):
        return OfertaEducativaCarrera.objects.filter(
            area_estudio=self,
            estatus=True,
        )


class OfertaEducativaCarrera(models.Model):
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "oferta_educativa_carrera"

    nombre = models.CharField(max_length=200)
    archivo_carrera = models.CharField(max_length=200, null=True)
    archivo_programa = models.CharField(max_length=200, null=True)
    estatus = models.BooleanField(default=True)
    area_estudio = models.ForeignKey(
        OfertaEducativaArea,
        on_delete=models.CASCADE,
        related_name="area_estudio",
    )


class PaginaCecyte(models.Model):
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "pagina_cecyte"

    nombre = models.CharField(max_length=200)
    objetivo = models.CharField(max_length=1000, null=True)
    carpeta = models.CharField(max_length=100, null=True)

    def get_contenido(self, estatus=None):
        data = ContenidoPagina.objects.filter(pagina_cecyte=self)
        if estatus:
            data.filter(estatus=estatus)
        return data


class ContenidoPagina(models.Model):
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "contenido_pagina"

    nombre = models.CharField(max_length=200)
    archivo_vista = models.CharField(max_length=200, null=True)
    texto = models.CharField(max_length=1000, null=True)
    pdf = models.CharField(max_length=200, null=True)
    imagen = models.CharField(max_length=200, null=True)
    estatus = models.BooleanField(default=True)
    pagina_cecyte = models.ForeignKey(
        PaginaCecyte,
        on_delete=models.CASCADE,
        related_name="contenido_pagina",
    )


class Estado(models.Model):
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "estado"

    nombre = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200)
    enlace = models.CharField(max_length=200, null=True)
    estatus = models.BooleanField(default=True)