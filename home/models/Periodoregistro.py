from django.db import models

class Periodoregistro(models.Model):
    def __str__(self):
        return self.periodo

    class Meta:
        db_table = "periodoregistrocuestionarios"

    periodo = models.CharField(max_length=45, null=True)
    fechainicio = models.DateField(null=True)
    fechafin = models.DateField(null=True)
    activo = models.BooleanField(default=True)
