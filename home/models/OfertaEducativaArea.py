from django.db import models


class OfertaEducativaArea(models.Model):
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "oferta_educativa_area"

    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField(default=True)
