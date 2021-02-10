from django.db import models
from .OfertaEducativaArea import OfertaEducativaArea


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
