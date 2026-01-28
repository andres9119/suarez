from django.shortcuts import render, get_object_or_404
from .models import ExperienciaCafetera

def lista_experiencias(request):
    experiencias = ExperienciaCafetera.objects.all()
    return render(request, 'experiencias_cafeteras/lista.html', {'experiencias': experiencias})

def detalle_experiencia(request, pk):
    experiencia = get_object_or_404(ExperienciaCafetera, pk=pk)
    return render(request, 'experiencias_cafeteras/detalle.html', {'experiencia': experiencia})
