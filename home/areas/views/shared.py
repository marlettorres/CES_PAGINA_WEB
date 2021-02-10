from home.models import ContenidoPagina, PaginaCecyte

def get_contenido_area(id):
    pagina_cecyte = PaginaCecyte.objects.get(id=id)
    elementos = ContenidoPagina.objects.filter(
        pagina_cecyte=pagina_cecyte,
        estatus=1,
    )

    return {
        "pagina_cecyte": pagina_cecyte,
        "ruta": pagina_cecyte.carpeta,
        "elementos": elementos,
    }
