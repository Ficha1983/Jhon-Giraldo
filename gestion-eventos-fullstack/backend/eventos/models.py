from django.db import models

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    descripcion = models.TextField(blank=True, null=True)  # Opcional

    def __str__(self):
        return self.nombre