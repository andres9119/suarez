from django.shortcuts import render
from .models import DocumentoPublico, CategoriaDocumento

def lista_documentos(request):
    categorias = CategoriaDocumento.objects.all()
    documentos = DocumentoPublico.objects.all()
    return render(request, 'documentos/lista.html', {
        'categorias': categorias,
        'documentos': documentos
    })
