from django.contrib import admin

# Register your models here.

from .models import (
    AreaCoordinacion,
    PersonaCoordinacion,
    PersonaColegio,
    MisionYVision,
    OfertaEducativaArea,
    OfertaEducativaCarrera,
    CatEntidades,
    CatPlanteles,
)

# Register your models here.
admin.site.register(AreaCoordinacion)
admin.site.register(PersonaCoordinacion)
admin.site.register(PersonaColegio)
admin.site.register(MisionYVision)
admin.site.register(OfertaEducativaArea)
admin.site.register(OfertaEducativaCarrera)
admin.site.register(CatEntidades)
admin.site.register(CatPlanteles)