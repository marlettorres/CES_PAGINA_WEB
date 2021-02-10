from django.db import models


class PlantelLegal(models.Model):
    class Meta:
        db_table = "encuesta_plantel_legal"

    encuesta_id = models.AutoField(primary_key=True)
    fecha = models.DateField(null=True)
    escritura_tiene = models.BooleanField(default=1, null=True)
    escritura_fecha = models.CharField(max_length=80, null=True)
    escritura_numero = models.CharField(max_length=80, null=True)
    escritura_volumen = models.CharField(max_length=80, null=True)
    comodato = models.CharField(max_length=80, null=True)
    arrendamiento = models.CharField(max_length=80, null=True)
    escrituracion = models.CharField(max_length=80, null=True)
    compraventa = models.CharField(max_length=80, null=True)
    presidencial = models.CharField(max_length=80, null=True)
    judicial = models.CharField(max_length=80, null=True)
    positiva = models.CharField(max_length=80, null=True)
