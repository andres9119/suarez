from django.contrib import admin
from .models import Comunidad, ImagenComunidad

class ImagenComunidadInline(admin.TabularInline):
    model = ImagenComunidad
    extra = 1

@admin.register(Comunidad)
class ComunidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo')
    list_filter = ('tipo',)
    search_fields = ('nombre', 'resena_cultural')
    inlines = [ImagenComunidadInline]
