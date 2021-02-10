from django.db import models


class OfertaEducativa(models.Model):
    class Meta:
        db_table = "encuesta_plantel_carrera"

    encuesta_id = models.AutoField(primary_key=True)
    fecha = models.DateField(null=True)
    encuesta_id = models.IntegerField(null=True)
    nombre = models.CharField(max_length=150, null=True)
    taller = models.BooleanField(default=1, null=True)
    nueva_operacion = models.BooleanField(default=1, null=True)
    dgp = models.BooleanField(default=1, null=True)
    refrendo = models.CharField(max_length=150, null=True)
    modalidad = models.CharField(max_length=150, null=True)
    opcion_educativa = models.CharField(max_length=150, null=True)
    grupos = models.IntegerField(null=True)
    turnos = models.CharField(max_length=150, null=True)
    hombres_primer = models.IntegerField(null=True)
    hombres_tercer = models.IntegerField(null=True)
    hombres_quinto = models.IntegerField(null=True)
    mujeres_primer = models.IntegerField(null=True)
    mujeres_tercer = models.IntegerField(null=True)
    mujeres_quinto = models.IntegerField(null=True)
