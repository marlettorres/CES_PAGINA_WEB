from django.db import models

class PaginaCecyte(models.Model):
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "pagina_cecyte"

    nombre = models.CharField(max_length=200)
    objetivo = models.CharField(max_length=1000, null=True)
    carpeta = models.CharField(max_length=100, null=True)