from django.db import models


class AreaCoordinacion(models.Model):
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "area_coordinacion"

    nombre = models.CharField(max_length=100)
    estatus = models.BooleanField(default=True)

    def get_personas(self):
        return PersonaCoordinacion.objects.filter(
            area_coordinacion=self,
            estatus=True,
        )


class PersonaCoordinacion(models.Model):
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "persona_coordinacion"

    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100, null=True)
    extension = models.CharField(max_length=10, null=True)
    correo = models.EmailField(max_length=100)
    estatus = models.BooleanField(default=True)
    imagen = models.CharField(max_length=100, null=True)
    area_coordinacion = models.ForeignKey(
        AreaCoordinacion,
        on_delete=models.CASCADE,
        related_name="personas",
    )


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


class MisionYVision(models.Model):
    class Meta:
        db_table = "mision_y_vision"

    mision = models.TextField(max_length=500)
    vision = models.TextField(max_length=500)
    estatus = models.BooleanField(default=True)


class OfertaEducativaArea(models.Model):
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "oferta_educativa_area"

    nombre = models.CharField(max_length=200)
    estatus = models.BooleanField(default=True)

    def get_carreras(self):
        return OfertaEducativaCarrera.objects.filter(
            area_estudio=self,
            estatus=True,
        )


class OfertaEducativaCarrera(models.Model):
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "oferta_educativa_carrera"

    nombre = models.CharField(max_length=200)
    archivo_carrera = models.CharField(max_length=200, null=True)
    archivo_programa = models.CharField(max_length=200, null=True)
    estatus = models.BooleanField(default=True)
    area_estudio = models.ForeignKey(
        OfertaEducativaArea,
        on_delete=models.CASCADE,
        related_name="area_estudio",
    )


class PaginaCecyte(models.Model):
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "pagina_cecyte"

    nombre = models.CharField(max_length=200)
    objetivo = models.CharField(max_length=1000, null=True)
    carpeta = models.CharField(max_length=100, null=True)

    def get_contenido(self, estatus=None):
        data = ContenidoPagina.objects.filter(pagina_cecyte=self)
        if estatus:
            data.filter(estatus=estatus)
        return data


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


class Estado(models.Model):
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "estado"

    nombre = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200)
    enlace = models.CharField(max_length=200, null=True)
    estatus = models.BooleanField(default=True)

class CatEntidades(models.Model):
    def __str__(self):
        return self.entidad

    class Meta:
        db_table = "catentidades"

    entidad = models.CharField(max_length=200)

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
class EncuestaPlantel(models.Model):
    class Meta:
        db_table = "encuesta_plantel2020"

    id = models.AutoField(primary_key=True)
    fecha = models.DateField(null=True)
    folio = models.CharField(max_length=50)
    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE,
        related_name="encuesta_plantel",
    )
    plantel = models.ForeignKey(
        CatPlanteles,
        on_delete=models.CASCADE,
        related_name="encuesta_plantel",
    )
class PlantelInformacion(models.Model):
    class Meta:
        db_table = "encuesta_plantel_info"
     
    encuesta_id = models.AutoField(primary_key=True)        
    fecha = models.DateField(null=True)
    latitud = models.FloatField(null=True)
    longitud = models.FloatField(null=True)
    calle = models.CharField(max_length=150, null=True)
    no_exterior = models.CharField(max_length=150, null=True)
    no_interior = models.CharField(max_length=150, null=True)
    colonia = models.CharField(max_length=150, null=True)
    municipio = models.CharField(max_length=150, null=True)
    localidad = models.CharField(max_length=150, null=True)
    entidad_federativa = models.CharField(max_length=150, null=True)
    codigo_postal = models.IntegerField(null=True)
    ciudad = models.CharField(max_length=150, null=True)
    telefono = models.CharField(max_length=150, null=True)
    pagina_web = models.CharField(max_length=150, null=True)
    correo_electronico = models.CharField(max_length=150, null=True)
    existen_planos = models.BooleanField(default=1, null=True)
    archivado_en = models.CharField(max_length=150, null=True)
    colinda_norte = models.CharField(max_length=150, null=True)
    colinda_sur = models.CharField(max_length=150, null=True)
    colinda_este = models.CharField(max_length=150, null=True)
    colinda_oeste = models.CharField(max_length=150, null=True)
    internet = models.BooleanField(default=1)
     
    # add in author later
class PlantelInfraestructura(models.Model):
    class Meta:
        db_table = "encuesta_plantel_infraestructura"

    encuesta_id = models.AutoField(primary_key=True)        
    fecha = models.DateField(null=True)
    niveles = models.CharField(max_length=150, null=True)
    superficie_total = models.CharField(max_length=150, null=True)
    superficie_libre = models.CharField(max_length=150, null=True)
    superficie_urbana = models.CharField(max_length=150, null=True)
    uso_plantel = models.CharField(max_length=150, null=True)
    conservacion = models.CharField(max_length=150, null=True)
    personas_laboran = models.IntegerField(null=True)
    aulas_tiene = models.BooleanField(default=1, null=True)
    aulas_funcionalidad = models.CharField(max_length=150, null=True)
    aulas_cantidad = models.IntegerField(null=True)
    laboratorios_tiene = models.BigIntegerField(null=True)
    laboratorios_funcionalidad = models.CharField(max_length=150, null=True)
    laboratorios_cantidad = models.IntegerField(null=True)
    laboratorios_especificar = models.CharField(max_length=150, null=True)
    talleres_tiene = models.BooleanField(default=1, null=True)
    talleres_funcionalidad = models.CharField(max_length=150, null=True)
    talleres_cantidad = models.IntegerField(null=True)
    talleres_especificar = models.CharField(max_length=150, null=True)
    salon_usos_multiple_tiene = models.BooleanField(default=1, null=True)
    salon_usos_multiple_funcionalidad = models.CharField(max_length=150, null=True)
    auditorio_tiene = models.BooleanField(default=1, null=True)
    auditorio_funcionalidad = models.CharField(max_length=150, null=True)
    biblioteca_tiene = models.BooleanField(default=1, null=True)
    biblioteca_funcionalidad = models.CharField(max_length=150, null=True)
    plaza_civica_tiene = models.BooleanField(default=1, null=True)
    plaza_civica_funcionalidad = models.CharField(max_length=150, null=True)
    plaza_civica_techada = models.CharField(max_length=150, null=True)
    plaza_civica_tipo = models.CharField(max_length=150, null=True)
    jardineras_tiene = models.BigIntegerField(null=True)
    jardineras_funcionalidad = models.CharField(max_length=150, null=True)
    areas_verdes_tiene = models.BooleanField(default=1, null=True)
    areas_verdes_funcionalidad = models.CharField(max_length=150, null=True)
    areas_verdes_metros = models.CharField(max_length=150, null=True)
    bebederos_tiene = models.BooleanField(default=1, null=True)
    bebederos_funcionalidad = models.CharField(max_length=150, null=True)
    rampa_tiene = models.BooleanField(default=1, null=True)
    rampa_funcionalidad = models.CharField(max_length=150, null=True)
    deportivas_tiene = models.BooleanField(default=1, null=True)
    deportivas_funcionalidad = models.CharField(max_length=150, null=True)
    futbol_soccer_tiene = models.BooleanField(default=1, null=True)
    futbol_soccer_funcionalidad = models.CharField(max_length=150, null=True)
    futbol_rapido_tiene = models.BooleanField(default=1, null=True)
    futbol_rapido_funcionalidad = models.CharField(max_length=150, null=True)
    basquetbol_tiene = models.BooleanField(default=1, null=True)
    basquetbol_funcionalidad = models.CharField(max_length=150, null=True)
    andadores_tiene = models.BooleanField(default=1, null=True)
    andadores_funcionalidad = models.CharField(max_length=150, null=True)
    andadores_cantidad = models.CharField(max_length=150, null=True)
    portico_tiene = models.BooleanField(default=1, null=True)
    portico_funcionalidad = models.CharField(max_length=150, null=True)
    cafeteria_tiene = models.BooleanField(default=1, null=True)
    cafeteria_funcionalidad = models.CharField(max_length=150, null=True)
    edificios_tiene = models.BooleanField(default=1, null=True)
    edificios_funcionalidad = models.CharField(max_length=150, null=True)
    modulos_administrativos_tiene = models.BooleanField(default=1, null=True)
    direccion_tiene = models.BooleanField(default=1, null=True)
    direccion_funcionalidad = models.CharField(max_length=150, null=True)
    control_escolar_tiene = models.BooleanField(default=1, null=True)
    control_escolar_funcionalidad = models.CharField(max_length=150, null=True)
    servicio_social_tiene = models.BooleanField(default=1, null=True)
    servicio_social_funcionalidad = models.CharField(max_length=150, null=True)
    prefectura_tiene = models.BooleanField(default=1, null=True)
    prefectura_funcionalidad = models.CharField(max_length=150, null=True)
    area_administrativa_tiene = models.BooleanField(default=1, null=True)
    area_administrativa_funcionalidad = models.CharField(max_length=150, null=True)
    area_academica_tiene = models.BooleanField(default=1, null=True)
    area_academica_funcionalidad = models.CharField(max_length=150, null=True)
    area_planeacion_tiene = models.BooleanField(default=1, null=True)
    area_planeacion_funcionalidad = models.CharField(max_length=150, null=True)
    area_vinculacion_tiene = models.BooleanField(default=1, null=True)
    area_vinculacion_funcionalidad = models.CharField(max_length=150, null=True)
    area_estres_tiene = models.BooleanField(default=1, null=True)
    area_estres_funcionalidad = models.CharField(max_length=150, null=True)
    sala_maestros_tiene = models.BooleanField(default=1, null=True)
    sala_maestros_funcionalidad = models.CharField(max_length=150, null=True)
    cerco_perimetral_tiene = models.BooleanField(default=1, null=True)
    cerco_perimetral_funcionalidad = models.CharField(max_length=150, null=True)
    cerco_perimetral_tipo = models.CharField(max_length=150, null=True)
    cerco_perimetral_metros = models.CharField(max_length=150, null=True)
    puertas_tiene = models.BooleanField(default=1, null=True)
    puertas_funcionalidad = models.CharField(max_length=150, null=True)
    caseta_vigilancia_tiene = models.BooleanField(default=1, null=True)
    caseta_vigilancia_funcionalidad = models.CharField(max_length=150, null=True)
    sistema_hidro_tiene = models.BooleanField(default=1, null=True)
    sistema_hidro_funcionalidad = models.CharField(max_length=150, null=True)
    estacion_elec_tiene = models.BooleanField(default=1, null=True)
    estacion_elec_funcionalidad = models.CharField(max_length=150, null=True)
    transformador_tiene = models.BooleanField(default=1, null=True)
    transformador_funcionalidad = models.CharField(max_length=150, null=True)
    tablero_tiene = models.BooleanField(default=1, null=True)
    tablero_funcionalidad = models.CharField(max_length=150, null=True)
    planta_energia_tiene = models.BooleanField(default=1, null=True)
    planta_energia_funcionalidad = models.CharField(max_length=150, null=True)
    cisterna_tiene = models.BooleanField(default=1, null=True)
    cisterna_funcionalidad = models.CharField(max_length=150, null=True)
    aire_tiene = models.BooleanField(default=1, null=True)
    aire_funcionalidad = models.CharField(max_length=150, null=True)
    minisplit_tiene = models.BooleanField(default=1, null=True)
    minisplit_funcionalidad = models.CharField(max_length=150, null=True)
    minisplit_cuantos = models.CharField(max_length=150, null=True)
    calefaccion_tiene = models.BooleanField(default=1, null=True)
    calefaccion_funcionalidad = models.CharField(max_length=150, null=True)
    calefaccion_cuantos = models.CharField(max_length=150, null=True)
    incendio_tiene = models.BooleanField(default=1, null=True)
    incendio_funcionalidad = models.CharField(max_length=150, null=True)
    incendio_cuantos = models.CharField(max_length=150, null=True)
    bombeo_tiene = models.BooleanField(default=1, null=True)
    bombeo_funcionalidad = models.CharField(max_length=150, null=True)
    bombeo_cuantos = models.CharField(max_length=150, null=True)
    humo_tiene = models.BooleanField(default=1, null=True)
    humo_funcionalidad = models.CharField(max_length=150, null=True)
    sismo_tiene = models.BooleanField(default=1, null=True)
    sismo_funcionalidad = models.CharField(max_length=150, null=True)
    sanitarios_estudiantes_tiene = models.BooleanField(default=1, null=True)
    sanitarios_estudiantes_funcionalidad =  models.CharField(max_length=150, null=True)
    sanitarios_estudiantes_hombre = models.IntegerField(null=True)
    sanitarios_estudiantes_mujer = models.IntegerField(null=True)
    sanitarios_docentes_tiene = models.BooleanField(default=1, null=True)
    sanitarios_docentes_funcionalidad = models.CharField(max_length=150, null=True)
    sanitarios_docentes_hombre = models.IntegerField(null=True)
    sanitarios_docentes_mujer = models.IntegerField(null=True)
    sanitarios_administrativos_tiene = models.BooleanField(default=1, null=True)
    sanitarios_administrativos_funcionalidad = models.CharField(max_length=150, null=True)
    sanitarios_administrativos_hombre = models.IntegerField(null=True)
    sanitarios_administrativos_mujer = models.IntegerField(null=True)
    fosa_tiene = models.BooleanField(default=1, null=True)
    fosa_funcionalidad = models.CharField(max_length=150, null=True)
    pozo_tiene = models.BooleanField(default=1, null=True)
    pozo_funcionalidad = models.CharField(max_length=150, null=True)
    drenaje_tiene = models.BooleanField(default=1, null=True)
    drenaje_funcionalidad = models.CharField(max_length=150, null=True)

class PlantelEstadistica(models.Model):
    class Meta:
        db_table = "encuesta_plantel_estadistica"
     
    encuesta_id = models.AutoField(primary_key=True)        
    fecha = models.DateField(null=True)
    dg_nombre = models.CharField(max_length=150, null=True)
    dg_ap_paterno = models.CharField(max_length=150, null=True)
    dg_ap_materno = models.CharField(max_length=150, null=True)
    dg_perfil_academico = models.CharField(max_length=150, null=True)
    dg_cedula = models.CharField(max_length=150, null=True)
    dg_fecha_nombramiento = models.CharField(max_length=150, null=True)
    dg_plaza = models.BooleanField(default=1, null=True)
    dg_plaza_antiguedad = models.CharField(max_length=150, null=True)
    dg_horas = models.CharField(max_length=150, null=True)
    equipo_computo_docente_con = models.IntegerField(null=True)
    equipo_computo_docente_sin = models.IntegerField(null=True)
    equipo_computo_administrativo_con = models.IntegerField(null=True)
    equipo_computo_administrativo_sin = models.IntegerField(null=True)
    equipo_computo_alumnos_con = models.IntegerField(null=True)
    equipo_computo_alumnos_sin = models.IntegerField(null=True)
    equipo_computo_compartido_con = models.IntegerField(null=True)
    equipo_computo_compartido_sin = models.IntegerField(null=True)
    equipo_computo_velocidad = models.CharField(max_length=150, null=True)

class PlantelEscolaridad(models.Model):
    class Meta:
        db_table = "encuesta_plantel_escolaridad"
     
    encuesta_id = models.AutoField(primary_key=True)        
    fecha = models.DateField(null=True)
    directivo_doctorado = models.IntegerField(null=True)
    docente_doctorado = models.IntegerField(null=True)
    administrativo_doctorado = models.IntegerField(null=True)
    servicios_doctorado = models.IntegerField(null=True)
    directivo_maestria = models.IntegerField(null=True)
    docente_maestria = models.IntegerField(null=True)
    administrativo_maestria = models.IntegerField(null=True)
    servicios_maestria = models.IntegerField(null=True)
    directivo_especializacion = models.IntegerField(null=True)
    docente_especializacion = models.IntegerField(null=True)
    administrativo_especializacion = models.IntegerField(null=True)
    servicios_especializacion = models.IntegerField(null=True)
    directivo_licenciatura = models.IntegerField(null=True)
    docente_licenciatura = models.IntegerField(null=True)
    administrativo_licenciatura = models.IntegerField(null=True)
    servicios_licenciatura = models.IntegerField(null=True)
    directivo_superior = models.IntegerField(null=True)
    docente_superior = models.IntegerField(null=True)
    administrativo_superior = models.IntegerField(null=True)
    servicios_superior = models.IntegerField(null=True)
    directivo_superior_maestros = models.IntegerField(null=True)
    docente_superior_maestros = models.IntegerField(null=True)
    administrativo_superior_maestros = models.IntegerField(null=True)
    servicios_superior_maestros = models.IntegerField(null=True)
    directivo_bachillerato = models.IntegerField(null=True)
    docente_bachillerato = models.IntegerField(null=True)
    administrativo_bachillerato = models.IntegerField(null=True)
    servicios_bachillerato = models.IntegerField(null=True)
    directivo_tecnico = models.IntegerField(null=True)
    docente_tecnico = models.IntegerField(null=True)
    administrativo_tecnico = models.IntegerField(null=True)
    servicios_tecnico = models.IntegerField(null=True)
    directivo_comercial = models.IntegerField(null=True)
    docente_comercial = models.IntegerField(null=True)
    administrativo_comercial = models.IntegerField(null=True)
    servicios_comercial = models.IntegerField(null=True)
    directivo_secundaria = models.IntegerField(null=True)
    docente_secundaria = models.IntegerField(null=True)
    administrativo_secundaria = models.IntegerField(null=True)
    servicios_secundaria = models.IntegerField(null=True)
    directivo_primaria = models.IntegerField(null=True)
    docente_primaria = models.IntegerField(null=True)
    administrativo_primaria = models.IntegerField(null=True)
    servicios_primaria = models.IntegerField(null=True)

class OfertaEducativa(models.Model):
    class Meta:
        db_table = "encuesta_plantel_carrera"
     
    encuesta_id = models.AutoField(primary_key=True)        
    fecha = models.DateField(null=True)
    encuesta_id = models.IntegerField(null=True)
    nombre = models.CharField(max_length=150, null=True)
    taller = models.BooleanField(default=1, null=True)
    nueva_operacion = models.BooleanField(default=1, null=True)
    dgp = models.BooleanField(default=1, null=True)
    refrendo = models.CharField(max_length=150, null=True)
    modalidad = models.CharField(max_length=150, null=True)
    opcion_educativa = models.CharField(max_length=150, null=True)
    grupos = models.IntegerField(null=True)
    turnos = models.CharField(max_length=150, null=True)
    hombres_primer = models.IntegerField(null=True)
    hombres_tercer = models.IntegerField(null=True)
    hombres_quinto = models.IntegerField(null=True)
    mujeres_primer = models.IntegerField(null=True)
    mujeres_tercer = models.IntegerField(null=True)
    mujeres_quinto = models.IntegerField(null=True)

class PlantelLegal(models.Model):
    class Meta:
        db_table = "encuesta_plantel_legal"
     
    encuesta_id = models.AutoField(primary_key=True)        
    fecha = models.DateField(null=True)
    escritura_tiene = models.BooleanField(default=1, null=True)
    escritura_fecha = models.CharField(max_length=80, null=True)
    escritura_numero = models.CharField(max_length=80, null=True)
    escritura_volumen = models.CharField(max_length=80, null=True)
    comodato = models.CharField(max_length=80, null=True)
    arrendamiento = models.CharField(max_length=80, null=True)
    escrituracion = models.CharField(max_length=80, null=True)
    compraventa = models.CharField(max_length=80, null=True)
    presidencial = models.CharField(max_length=80, null=True)
    judicial = models.CharField(max_length=80, null=True)
    positiva = models.CharField(max_length=80, null=True)

class PlantelVinculacion(models.Model):
    class Meta:
        db_table = "encuesta_plantel_vinculacion"
     
    encuesta_id = models.AutoField(primary_key=True)        
    fecha = models.DateField(null=True)
    mfd = models.BooleanField(default=1, null=True)
    convenios = models.CharField(max_length=150, null=True)
    mfd_camara = models.BooleanField(default=1, null=True)
    mfd_alumnos = models.CharField(max_length=150, null=True)
    mfd_beca = models.CharField(max_length=150, null=True)
    convenios_publicas = models.CharField(max_length=150, null=True)
    convenios_privadas = models.CharField(max_length=150, null=True)
    convenios_servicio = models.CharField(max_length=150, null=True)
    convenios_practicas = models.CharField(max_length=150, null=True)
    redes_sociales = models.CharField(max_length=150, null=True)
    alumnos_creatividad = models.CharField(max_length=150, null=True)
    alumnos_arte = models.CharField(max_length=150, null=True)
    equipos_deportivos = models.CharField(max_length=150, null=True)
    disciplinas = models.CharField(max_length=150, null=True)
    comite_estatal = models.BooleanField(default=1, null=True)
    comite_regional = models.BooleanField(default=1, null=True)
    emprendimiento = models.BooleanField(default=1, null=True)
    alumnos_benito = models.CharField(max_length=150, null=True)
    alumnos_benito_porcentaje = models.CharField(max_length=150, null=True)
    alumnos_beca_dual = models.CharField(max_length=150, null=True)
    alumnos_beca_servicio = models.CharField(max_length=150, null=True)
    alumnos_beca_practicas = models.CharField(max_length=150, null=True)
    docentes_beca = models.CharField(max_length=150, null=True)
    egresados_2016 = models.CharField(max_length=150, null=True)
    egresados_2017 = models.CharField(max_length=150, null=True)
    egresados_2017_superior = models.CharField(max_length=150, null=True)
    egresados_2017_laboral = models.CharField(max_length=150, null=True)
    sectores_productos = models.CharField(max_length=150, null=True)
  
  