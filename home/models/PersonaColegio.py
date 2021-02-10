from django.db import models

class PersonaColegio(models.Model):
    def __str__(self):
        return self.estado

    class Meta:
        db_table = "persona_colegio"

    estado = models.CharField(max_length=100)
    director_general = models.CharField(max_length=100)
    direccion = models.TextField(max_length=200, null=True)
    telefono = models.CharField(max_length=50, null=True)
    estatus = models.BooleanField(default=True)
