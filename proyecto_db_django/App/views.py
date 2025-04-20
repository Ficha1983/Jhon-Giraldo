from rest_framework import viewsets
from .models import Producto  # Importa el modelo Producto
from .serializers import ProductoSerializer  # Importa el serializador ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):  # Define una vista basada en el conjunto de vistas de modelo
    queryset = Producto.objects.all()  # Obtiene todos los objetos de Producto
    serializer_class = ProductoSerializer  # Especifica el serializador a utilizar  
    # Create your views here.
