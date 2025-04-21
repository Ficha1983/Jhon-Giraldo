from bson import ObjectId
from mongo_conexion import obtener_db
def obtener_categorias():
    db = obtener_db()
    return list(db.categorias.find())

def obtener_categoria_por_id(id):
    db = obtener_db()
    return db.categorias.find_one({"_id": ObjectId(id)})

def crear_categoria(nombre, descripcion):
    db = obtener_db()
    resultado = db.categorias.insert_one({"nombre": nombre, "descripcion":
    descripcion})
    return obtener_categoria_por_id(resultado.inserted_id)

def actualizar_categoria(id, nuevos_datos):
    db = obtener_db()
    db.categorias.update_one({"_id": ObjectId(id)}, {"$set": nuevos_datos})
    return obtener_categoria_por_id(id)

def eliminar_categoria(id):
    db = obtener_db()
    return db.categorias.delete_one({"_id": ObjectId(id)}).deleted_count == 1