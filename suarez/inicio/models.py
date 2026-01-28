from django.db import models

class BannerPrincipal(models.Model):
    titulo = models.CharField(max_length=200, default="Bienvenidos a Suárez")
    subtitulo = models.TextField(default="Portal Institucional de la Alcaldía Municipal.")
    imagen_fondo = models.ImageField(upload_to='banner/', help_text="Imagen de gran tamaño para el fondo del banner")
    texto_boton = models.CharField(max_length=50, default="Ver Noticias")
    link_boton = models.CharField(max_length=200, default="/noticias/")
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Banner Principal"
        verbose_name_plural = "Banner Principal"

    def __str__(self):
        return self.titulo


class Video(models.Model):
    titulo = models.CharField(max_length=200)
    url_embebida = models.URLField(help_text="URL de YouTube para embeber (ej. https://www.youtube.com/embed/...)")
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class ImagenGaleria(models.Model):
    titulo = models.CharField(max_length=200, blank=True)
    imagen = models.ImageField(upload_to='galeria/')
    es_destacada = models.BooleanField(default=False, help_text="Si se marca, aparecerá en el carrusel de la página de inicio")
    fecha_carga = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.titulo or f"Imagen {self.id}"

class EventoDestacado(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='eventos_destacados/')
    fecha_evento = models.DateField()
    link = models.URLField(blank=True, null=True, help_text="Link opcional a más información")

    def __str__(self):
        return self.titulo
