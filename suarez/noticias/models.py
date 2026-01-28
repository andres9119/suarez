from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="Identificador único para la URL (ej. nueva-obra-en-el-pueblo)")
    contenido = models.TextField()
    imagen_destacada = models.ImageField(upload_to='noticias/')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    es_evento = models.BooleanField(default=False, help_text="Marcar si es un evento municipal")
    fecha_evento = models.DateField(blank=True, null=True, help_text="Solo si es un evento")

    class Meta:
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return self.titulo
