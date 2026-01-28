from django.db import models

class ExperienciaCafetera(models.Model):
    titulo = models.CharField(max_length=200)
    historia = models.TextField()
    proceso = models.TextField(help_text="Descripción del proceso de producción o preparación")
    imagen_principal = models.ImageField(upload_to='cafe/imagenes/')
    video_url = models.URLField(blank=True, null=True, help_text="URL de video relacionado")
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
