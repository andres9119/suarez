from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('noticias/', include('noticias.urls')),
    path('comunidades/', include('comunidades.urls')),
    path('experiencias-cafeteras/', include('experiencias_cafeteras.urls')),
    path('documentos/', include('documentos.urls')),
    path('contacto/', include('contacto.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
