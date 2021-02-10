from django.db import models


class Estado(models.Model):
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "estado"

    nombre = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200)
    enlace = models.CharField(max_length=200, null=True)
    estatus = models.BooleanField(default=True)
