from django.db import models  # Importa el módulo 'models' de Django que permite crear modelos de base de datos

class Producto(models.Model): # Define una clase llamada 'Producto' que hereda de models.Model (es decir, es un modelo de Django)
    nombre = models.CharField(max_length=100) # Campo de texto para el nombre del producto (hasta 100 caracteres)
    precio = models.DecimalField(max_digits=10, decimal_places=2) # Campo para el precio del producto con hasta 10 dígitos en total, y 2 después del punto decimal
    descripcion = models.TextField() # Campo de texto largo para una descripción del producto
    fecha_creacion = models.DateTimeField(auto_now_add=True) # Campo que guarda automáticamente la fecha y hora en la que se creó el producto

    def __str__(self):
        return self.nombre

# Create your models here.
# Comentario por defecto de Django indicando dónde crear modelos
# Create your models here.