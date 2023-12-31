from django.shortcuts import render

from home.models import ContenidoPagina, PaginaCecyte, ImagenNoticia


def inicio_view(request):
    context = get_contenido_inicio()
    response = render(request, "inicio/inicio.html", context)
    response['Server'] = 'dev'
    return response


def get_contenido_inicio():
    AREAID_BANNERS = 4
    AREAID_ANUNCIOS = 5
    AREAID_NOTICIAS = 6

    IMAGENID = 55 

    pagina_banners = PaginaCecyte.objects.get(id=AREAID_BANNERS)
    pagina_anuncios = PaginaCecyte.objects.get(id=AREAID_ANUNCIOS)
    pagina_noticias = PaginaCecyte.objects.get(id=AREAID_NOTICIAS)

    elementos_banners = ContenidoPagina.objects.filter(
        pagina_cecyte=pagina_banners,
        estatus=1,
    )
    elementos_anuncios = ContenidoPagina.objects.filter(
        pagina_cecyte=pagina_anuncios,
        estatus=1,
    )
    elementos_noticias = ContenidoPagina.objects.filter(
        pagina_cecyte=pagina_noticias,
        estatus=1,
    )
    datos=[]
    for elemento in elementos_noticias:
        elementos_imagenes = elemento.imagenes_noticia.all()
        datos.append([elemento,elementos_imagenes])
    datos=datos
    return {
        "elementos_banners": elementos_banners,
        "elementos_anuncios": elementos_anuncios,
        "elementos_noticias": elementos_noticias,
        "elementos_imagenes":elementos_imagenes,
        "datos":datos,
        "ruta_banners": pagina_banners.carpeta,
        "ruta_anuncios": pagina_anuncios.carpeta,
        "ruta_noticias": pagina_noticias.carpeta,
    }
