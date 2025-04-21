from pymongo import MongoClient
def obtener_db():
    cliente = MongoClient("mongodb://localhost:27017/")
    return cliente["tiendavirtual"]