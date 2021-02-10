from django.db import models
from .AreaCoordinacion import AreaCoordinacion


class PersonaCoordinacion(models.Model):
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "persona_coordinacion"

    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100, null=True)
    extension = models.CharField(max_length=10, null=True, blank=True)
    correo = models.EmailField(max_length=100)
    estatus = models.BooleanField(default=True)
    imagen = models.CharField(max_length=100, null=True, blank=True)
    area_coordinacion = models.ForeignKey(
        AreaCoordinacion,
        on_delete=models.CASCADE,
        related_name="personas",
    )
