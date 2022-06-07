from django.db import models
from .ContenidoPagina import ContenidoPagina

class ImagenNoticia(models.Model):
    def __str__(self):
        return self.imagenes 

    class Meta:
        db_table = "imagenes_noticia"
        
    imagenes = models.TextField()
    contenido_pagina = models.ForeignKey(
        ContenidoPagina,
        on_delete=models.CASCADE,
        related_name="imagenes_noticia",
    )
