from bson import ObjectId
from datetime import datetime
from mongo_conexion import obtener_db
def obtener_productos():
    db = obtener_db()
    return list(db.productos.find())

def obtener_producto_por_id(id):
    db = obtener_db()
    return db.productos.find_one({"_id": ObjectId(id)})

def crear_producto(nombre, descripcion, precio, stock, categoria_id, tallas,
    colores):
    db = obtener_db()
    producto = {
    "nombre": nombre,
    "descripcion": descripcion,
    "precio": precio,
    "stock": stock,
    "categoriaId": ObjectId(categoria_id),
    "tallas": tallas,
    "colores": colores,
    "fechaCreacion": datetime.now()
    }
    resultado = db.productos.insert_one(producto)
    return obtener_producto_por_id(resultado.inserted_id)

def actualizar_producto(id, nuevos_datos):
    db = obtener_db()
    db.productos.update_one({"_id": ObjectId(id)}, {"$set": nuevos_datos})
    return obtener_producto_por_id(id)

def eliminar_producto(id):
    db = obtener_db()
    return db.productos.delete_one({"_id": ObjectId(id)}).deleted_count == 1
