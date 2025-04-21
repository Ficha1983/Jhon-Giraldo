from producto_crud import *
# Crear producto de prueba
categoria_id = "605c72b44f1c2f1d4c8b4567" # Reemplaza con ID real
producto = crear_producto(
"Abono orgánico",
"Producto natural para plantas",
18000,
20,
categoria_id,
["S", "M"],
["Verde", "Marrón"]
)
print(producto)