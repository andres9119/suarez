from django.db import models

class Comunidad(models.Model):
    TIPO_CHOICES = [
        ('indigena', 'Indígena'),
        ('afro', 'Afrodescendiente'),
        ('campesina', 'Campesina'),
    ]
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    resena_cultural = models.TextField()
    historia = models.TextField()
    logo_o_emblema = models.ImageField(upload_to='comunidades/logos/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"

class ImagenComunidad(models.Model):
    comunidad = models.ForeignKey(Comunidad, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='comunidades/galeria/')
    descripcion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Imagen de {self.comunidad.nombre}"
