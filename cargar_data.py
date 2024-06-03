import csv
from configuracion import crear_base

def cargar_datos_desde_csv(archivo_csv):
    db = crear_base()

    # Conexión a las colecciones
    coleccion_jugadores = db['jugadores']
    coleccion_partidos = db['partidos']
    coleccion_torneos = db['torneos']

    # Diccionario para mapear nombres de jugadores a sus ID en la base de datos
    ids_jugadores = {}

    # Abrir el archivo CSV y leer los datos
    with open(archivo_csv, 'r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo, delimiter=',')
        # Saltar la primera fila (encabezados)
        next(lector)
        # Iterar sobre cada fila del CSV
        for fila in lector:
            # Crear documento para el jugador 1
            jugador_1 = {
                "nombre": fila['Player_1'],
                "ranking": int(fila['Rank_1']),
                "puntos": int(fila['Pts_1'])
            }
            # Insertar jugador 1 en la colección de jugadores y guardar su ID
            id_jugador_1 = coleccion_jugadores.insert_one(jugador_1).inserted_id
            ids_jugadores[fila['Player_1']] = id_jugador_1

            # Crear documento para el jugador 2
            jugador_2 = {
                "nombre": fila['Player_2'],
                "ranking": int(fila['Rank_2']),
                "puntos": int(fila['Pts_2'])
            }
            # Insertar jugador 2 en la colección de jugadores y guardar su ID
            id_jugador_2 = coleccion_jugadores.insert_one(jugador_2).inserted_id
            ids_jugadores[fila['Player_2']] = id_jugador_2

            # Crear documento para el partido
            partido = {
                "torneo": fila['Tournament'],
                "jugador_1": ids_jugadores[fila['Player_1']],
                "jugador_2": ids_jugadores[fila['Player_2']],
                "ganador": ids_jugadores[fila['Winner']],
                "resultado": fila['score'],
                "ronda": fila['Round'],
                "numero_set": fila['Best of'],
                "cuota1": fila['Odd_1'],
                "cuota2": fila['Odd_2']
            }
            # Insertar partido en la colección de partidos
            coleccion_partidos.insert_one(partido)

            # Crear documento para el torneo si no existe
            torneo = {
                "nombre": fila['Tournament'],
                "fecha": fila['Date'],
                "superficie": fila['Surface'],
                "categoria": fila['Series'],
                "ubicacion": fila['Court']
            }
            # Insertar torneo si no existe en la colección de torneos
            coleccion_torneos.update_one({"nombre": fila['Tournament']}, {"$setOnInsert": torneo}, upsert=True)

    print("Datos cargados con éxito en la base de datos")

if __name__ == "__main__":
    archivo_csv = "data/atp_tennis.csv"
    cargar_datos_desde_csv(archivo_csv)
