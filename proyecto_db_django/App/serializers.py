from rest_framework import serializers 
from .models import Producto # Importa el módulo serializers de Django REST Framework para crear serializadores

class ProductoSerializer(serializers.ModelSerializer): # Serializador para el modelo Producto
    class Meta:
        model = Producto
        fields = '__all__' # Especifica que se deben incluir todos los campos del modelo Producto
