import json
import os
import pygame
import constantes

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


def mostrar_ranking(pantalla:int):
    """Muestra el ranking en una ventana de Pygame"""
    partidas = leer_ranking()

    fuente_titulo = pygame.font.SysFont("Arial", 40)
    fuente_texto = pygame.font.SysFont("Arial", 28)

    fondo = pygame.transform.scale(constantes.FONDO, (constantes.ANCHO_PANTALLA, constantes.ALTO_PANTALLA))

    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                corriendo = False  # salir con ESC

        pantalla.blit(fondo, (0, 0))

        # título
        titulo = fuente_titulo.render("RANKING DE PARTIDAS", True, constantes.BLANCO)
        pantalla.blit(titulo, (constantes.ANCHO_PANTALLA//2 - titulo.get_width()//2, 50))

        # mostrar partidas
        y = 240
        for i, partida in enumerate(partidas[-5:], 1):  # últimas 5 partidas
            texto = f"{i}. {partida['jugador']} vs {partida['rival']} --->   Ganador: {partida['ganador']}"
            superficie = fuente_texto.render(texto, True, constantes.BLANCO)
            pantalla.blit(superficie, (200, y))
            y += 55

        pygame.display.flip()
