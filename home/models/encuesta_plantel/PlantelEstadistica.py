from django.db import models


class PlantelEstadistica(models.Model):
    class Meta:
        db_table = "encuesta_plantel_estadistica"

    encuesta_id = models.AutoField(primary_key=True)
    fecha = models.DateField(null=True)
    dg_nombre = models.CharField(max_length=150, null=True)
    dg_ap_paterno = models.CharField(max_length=150, null=True)
    dg_ap_materno = models.CharField(max_length=150, null=True)
    dg_perfil_academico = models.CharField(max_length=150, null=True)
    dg_cedula = models.CharField(max_length=150, null=True)
    dg_fecha_nombramiento = models.CharField(max_length=150, null=True)
    dg_plaza = models.BooleanField(default=1, null=True)
    dg_plaza_antiguedad = models.CharField(max_length=150, null=True)
    dg_horas = models.CharField(max_length=150, null=True)
    equipo_computo_docente_con = models.IntegerField(null=True)
    equipo_computo_docente_sin = models.IntegerField(null=True)
    equipo_computo_administrativo_con = models.IntegerField(null=True)
    equipo_computo_administrativo_sin = models.IntegerField(null=True)
    equipo_computo_alumnos_con = models.IntegerField(null=True)
    equipo_computo_alumnos_sin = models.IntegerField(null=True)
    equipo_computo_compartido_con = models.IntegerField(null=True)
    equipo_computo_compartido_sin = models.IntegerField(null=True)
    equipo_computo_velocidad = models.CharField(max_length=150, null=True)
