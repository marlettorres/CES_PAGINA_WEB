from django.db import models


class PlantelVinculacion(models.Model):
    class Meta:
        db_table = "encuesta_plantel_vinculacion"

    encuesta_id = models.AutoField(primary_key=True)
    fecha = models.DateField(null=True)
    mfd = models.BooleanField(default=1, null=True)
    convenios = models.CharField(max_length=150, null=True)
    mfd_camara = models.BooleanField(default=1, null=True)
    mfd_alumnos = models.CharField(max_length=150, null=True)
    mfd_beca = models.CharField(max_length=150, null=True)
    convenios_publicas = models.CharField(max_length=150, null=True)
    convenios_privadas = models.CharField(max_length=150, null=True)
    convenios_servicio = models.CharField(max_length=150, null=True)
    convenios_practicas = models.CharField(max_length=150, null=True)
    redes_sociales = models.CharField(max_length=150, null=True)
    alumnos_creatividad = models.CharField(max_length=150, null=True)
    alumnos_arte = models.CharField(max_length=150, null=True)
    equipos_deportivos = models.CharField(max_length=150, null=True)
    disciplinas = models.CharField(max_length=150, null=True)
    comite_estatal = models.BooleanField(default=1, null=True)
    comite_regional = models.BooleanField(default=1, null=True)
    emprendimiento = models.BooleanField(default=1, null=True)
    alumnos_benito = models.CharField(max_length=150, null=True)
    alumnos_benito_porcentaje = models.CharField(max_length=150, null=True)
    alumnos_beca_dual = models.CharField(max_length=150, null=True)
    alumnos_beca_servicio = models.CharField(max_length=150, null=True)
    alumnos_beca_practicas = models.CharField(max_length=150, null=True)
    docentes_beca = models.CharField(max_length=150, null=True)
    egresados_2016 = models.CharField(max_length=150, null=True)
    egresados_2017 = models.CharField(max_length=150, null=True)
    egresados_2017_superior = models.CharField(max_length=150, null=True)
    egresados_2017_laboral = models.CharField(max_length=150, null=True)
    sectores_productos = models.CharField(max_length=150, null=True)
