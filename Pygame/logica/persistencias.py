
import json
import os

archivo_ranking = "ranking.json"

def guardar_partida(jugador:str, rival:str, ganador:str)->list:
    """Guarda la partida en el archivo de ranking
    y devuelve la lista actualizada de partidas"""

    partida = {
        "jugador": jugador,
        "rival": rival,
        "ganador": ganador
    }

    if os.path.exists(archivo_ranking):
        with open(archivo_ranking, "r") as f:
            datos = json.load(f)
    else:
        datos = []

    datos.append(partida)

    with open(archivo_ranking, "w") as f:
        json.dump(datos, f, indent=4)


def leer_ranking():
    """Lee y devuelve todas las partidas guardadas"""
    if os.path.exists(archivo_ranking):
        with open(archivo_ranking, "r") as f:
            return json.load(f)
    return []