from django.db import models
from .PaginaCecyte import PaginaCecyte

class ContenidoPagina(models.Model):
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "contenido_pagina"

    nombre = models.CharField(max_length=200)
    archivo_vista = models.CharField(max_length=200, null=True)
    texto = models.CharField(max_length=1000, null=True)
    pdf = models.CharField(max_length=200, null=True)
    imagen = models.CharField(max_length=200, null=True)
    estatus = models.BooleanField(default=True)
    pagina_cecyte = models.ForeignKey(
        PaginaCecyte,
        on_delete=models.CASCADE,
        related_name="contenido_pagina",
    )
