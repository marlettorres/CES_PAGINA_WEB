from django.db import models

class MisionYVision(models.Model):
    class Meta:
        db_table = "mision_y_vision"

    mision = models.TextField(max_length=500)
    vision = models.TextField(max_length=500)
    estatus = models.BooleanField(default=True)
