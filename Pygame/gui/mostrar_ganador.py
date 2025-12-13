import pygame
import constantes
def mostrar_ganador(nombre):
    fuente = pygame.font.SysFont("arial",60)
    texto = fuente.render(f"¡{nombre} ha ganado la partida!",True, constantes.BLANCO)

    fondo = pygame.Surface((constantes.ANCHO_PANTALLA, constantes.ALTO_PANTALLA))