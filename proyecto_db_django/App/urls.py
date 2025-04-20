from django.urls import path, include  # Importa las funciones necesarias para definir rutas en Django
from rest_framework.routers import DefaultRouter  # Importa el enrutador por defecto de Django REST Framework
from .views import ProductoViewSet  # Importa el conjunto de vistas para el modelo Producto
# Crea un enrutador y registra el conjunto de vistas ProductoViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)  
urlpatterns = [
    path('', include(router.urls)),  # Incluye las rutas del enrutador en la URL principal
]

