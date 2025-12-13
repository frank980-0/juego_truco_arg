from logica.persistencias import leer_ranking
import pygame
import constantes

# parte visual de las persistencias del ranking

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
