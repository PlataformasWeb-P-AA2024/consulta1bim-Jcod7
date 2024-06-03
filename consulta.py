from cargar_data import cargar_datos_desde_csv
from configuracion import crear_base

# Archivo CSV con los datos
archivo_csv = "data/atp_tennis.csv"

# Cargar datos desde el archivo CSV a la base de datos
cargar_datos_desde_csv(archivo_csv)

# Crear una función para realizar consultas
def consultar_datos():
    # Crear conexión a la base de datos
    db = crear_base()

    # Ejemplo 1: Mostrar todos los torneos, con filtro opcional por ubicación específica, incluyendo la fecha 2022-07-25
    print("\nTodos los torneos con fecha 2022-07-25 y ubicación Outdoor:")
    torneos = db['torneos'].find(
        {"fecha": "2022-07-25", "ubicacion": "Outdoor"}
    )
    for torneo in torneos:
        print("Nombre:", torneo["nombre"])
        print("Fecha:", torneo["fecha"])
        print("Superficie:", torneo["superficie"])
        print("Categoría:", torneo["categoria"])
        print("Ubicación:", torneo["ubicacion"])
        print()

    print("****************************************************************************************************")

    # Ejemplo 2: Obtener el nombre, ranking y puntos de todos los jugadores cuyo ranking sea igual a 20, puntos igual a 1905 y nombre "Coric B."
    print("\nJugadores con ranking igual a 20, puntos igual a 1905, y nombre 'Coric B.':")
    jugadores = db['jugadores'].find(
        {"ranking": 20, "puntos": 1905, "nombre": "Coric B."}
    )
    for jugador in jugadores:
        print("Nombre:", jugador["nombre"])
        print("Ranking:", jugador["ranking"])
        print("Puntos:", jugador["puntos"])
        print()

    print("****************************************************************************************************")

    # Ejemplo 3: Mostrar todos los partidos en los que el resultado haya sido 6-2 6-2 con cuota 1 de 1.57
    print("\nTodos los partidos con resultado 6-2 6-2 y cuota 1 de 1.57:")
    partidos = db['partidos'].find(
        {"resultado": "6-2 6-2   ", 
         "cuota1": "1.57"}
    )
    for partido in partidos:
        print("Torneo:", partido["torneo"])
        print("Jugador 1:", partido["jugador_1"])
        print("Jugador 2:", partido["jugador_2"])
        print("Ganador:", partido["ganador"])
        print("Resultado:", partido["resultado"])
        print("Ronda:", partido["ronda"])
        print("Número de set:", partido["numero_set"])
        print("Cuota 1:", partido["cuota1"])
        print("Cuota 2:", partido["cuota2"])
        print()

# Ejecutar consultas
consultar_datos()
