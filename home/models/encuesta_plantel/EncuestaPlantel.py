from django.db import models
from home.models.Estado import Estado
from home.models.CatPlanteles import CatPlanteles
from home.models.Periodoregistro import Periodoregistro

class EncuestaPlantel(models.Model):
    class Meta:
        db_table = "encuesta_plantel2020"

    id = models.AutoField(primary_key=True)
    fecha = models.DateField(null=True)
    folio = models.CharField(max_length=50)
    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE,
        related_name="encuesta_plantel",
    )
    plantel = models.ForeignKey(
        CatPlanteles,
        on_delete=models.CASCADE,
        related_name="encuesta_plantel",
    )
    periodo = models.ForeignKey(
        Periodoregistro,
        on_delete=models.CASCADE,
        related_name="encuesta_plantel",
    )

