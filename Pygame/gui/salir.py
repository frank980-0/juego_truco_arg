import pygame
import constantes

def mostrar_salir(pantalla):

    while True:
        pantalla.blit(constantes.FONDO, (0, 0))
        fuente_titulo = pygame.font.Font(None, 74)
        texto_sombra = fuente_titulo.render("gracias por jugar", True, (0, 0, 0))
        texto = fuente_titulo.render("gracias por jugar", True, constantes.BLANCO)
        rect_texto = texto.get_rect(center=(constantes.ANCHO_PANTALLA * 0.5, constantes.ALTO_PANTALLA * 0.5))

        pantalla.blit(texto_sombra, (rect_texto.x + 6, rect_texto.y + 6))
        pantalla.blit(texto, rect_texto)

        pygame.display.flip()
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return