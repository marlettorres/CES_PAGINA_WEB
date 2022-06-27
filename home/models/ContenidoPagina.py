from django.db import models
from .PaginaCecyte import PaginaCecyte

class ContenidoPagina(models.Model):
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "contenido_pagina" 

    nombre = models.CharField(max_length=200)
    descripcion_breve = models.TextField()
    archivo_vista = models.CharField(max_length=200, null=True)
    texto = models.TextField()
    pdf = models.CharField(max_length=200, null=True)
    imagen = models.CharField(max_length=200, null=True)
    estatus = models.BooleanField(default=True)
    video = models.CharField(max_length=200, null=True) 
    opcion_video = models.IntegerField(null=True)
    pagina_cecyte = models.ForeignKey(
        PaginaCecyte,
        on_delete=models.CASCADE,
        related_name="contenido_pagina",
    )
