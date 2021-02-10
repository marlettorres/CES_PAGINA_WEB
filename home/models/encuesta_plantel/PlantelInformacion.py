from django.db import models


class PlantelInformacion(models.Model):
    class Meta:
        db_table = "encuesta_plantel_info"

    encuesta_id = models.AutoField(primary_key=True)
    fecha = models.DateField(null=True)
    latitud = models.FloatField(null=True)
    longitud = models.FloatField(null=True)
    calle = models.CharField(max_length=150, null=True)
    no_exterior = models.CharField(max_length=150, null=True)
    no_interior = models.CharField(max_length=150, null=True)
    colonia = models.CharField(max_length=150, null=True)
    municipio = models.CharField(max_length=150, null=True)
    localidad = models.CharField(max_length=150, null=True)
    entidad_federativa = models.CharField(max_length=150, null=True)
    codigo_postal = models.IntegerField(null=True)
    ciudad = models.CharField(max_length=150, null=True)
    telefono = models.CharField(max_length=150, null=True)
    pagina_web = models.CharField(max_length=150, null=True)
    correo_electronico = models.CharField(max_length=150, null=True)
    existen_planos = models.BooleanField(default=1, null=True)
    archivado_en = models.CharField(max_length=150, null=True)
    colinda_norte = models.CharField(max_length=150, null=True)
    colinda_sur = models.CharField(max_length=150, null=True)
    colinda_este = models.CharField(max_length=150, null=True)
    colinda_oeste = models.CharField(max_length=150, null=True)
    internet = models.BooleanField(default=1)

