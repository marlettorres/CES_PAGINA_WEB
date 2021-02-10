from django.db import models


class AreaCoordinacion(models.Model):
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "area_coordinacion"

    nombre = models.CharField(max_length=100)
    estatus = models.BooleanField(default=True)
