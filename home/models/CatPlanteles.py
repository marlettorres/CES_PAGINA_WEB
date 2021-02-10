from django.db import models
from .Estado import Estado


class CatPlanteles(models.Model):
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "plantel"

    cct = models.CharField(max_length=10, null=True)
    nombre = models.CharField(max_length=100, null=True)
    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE,
        related_name="plantel",
    )
