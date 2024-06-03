from pymongo import MongoClient

def crear_base():
    # Dirección del servidor, nos conectamos a través
    # del protocolo mongodb a nuestro servidor
    dbUrl = MongoClient('mongodb://localhost:27017/')
    # Creamos la base de datos consulta_01
    db = dbUrl['consulta_01']
    # Creamos la colección jugadores
    return db

if __name__ == "__main__":   
    db = crear_base()
    print("La base de datos consulta_01 se ha creado con éxito")
    # Intentar imprimir el nombre de la base de datos
    print("Nombre de la base de datos:", db.name)
