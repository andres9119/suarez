from django.shortcuts import render, get_object_or_404
from .models import Noticia

def lista_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias/lista.html', {'noticias': noticias})

def detalle_noticia(request, slug):
    noticia = get_object_or_404(Noticia, slug=slug)
    return render(request, 'noticias/detalle.html', {'noticia': noticia})
