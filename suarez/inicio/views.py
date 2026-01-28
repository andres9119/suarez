from django.shortcuts import render
from .models import Video, ImagenGaleria, EventoDestacado, BannerPrincipal

def home(request):
    banner = BannerPrincipal.objects.filter(activo=True).first()
    videos = Video.objects.all()[:3]
    # Featured images for carousel
    imagenes_carousel = ImagenGaleria.objects.filter(es_destacada=True)
    # Remaining images for grid (optional, but requested for carousel mostly)
    eventos = EventoDestacado.objects.all()[:3]
    
    return render(request, 'inicio/home.html', {
        'banner': banner,
        'videos': videos,
        'imagenes': imagenes_carousel,
        'eventos': eventos
    })

