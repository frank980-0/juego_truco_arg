import constantes
import pygame

def mostrar_mano(cartas_jugador: list, cartas_rival: list)->list:
    """
    Dibuja las cartas del jugador y del rival en pantalla,
    se crea la lista cartas_jugador_rects para manejar el hover
    """
    corriendo = True
    
    fondo = pygame.transform.scale(constantes.FONDO, (constantes.ANCHO_PANTALLA, constantes.ALTO_PANTALLA))
    
    cartas_jugador_rects = []
    for i, carta in enumerate(cartas_jugador):
        x = 200 + i * 120
        y = 400
        rect = pygame.Rect(x, y, 80, 120)
        cartas_jugador_rects.append((carta, rect))

    while corriendo:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        mouse_pos = pygame.mouse.get_pos()
        constantes.PANTALLA.blit(fondo, (0, 0))

        # mostrar cartas del jugador (abajo)
        for carta, rect in cartas_jugador_rects:
            numero, palo = carta
            ruta = constantes.RUTA_CARTA.format(numero=numero, palo=palo)
            img = pygame.image.load(ruta)
            img = pygame.transform.scale(img, (80, 120))

            # hover: si el mouse está encima, subo la carta

            draw_rect = rect.copy() # se crea una copia para no modificar el rect original
            if draw_rect.collidepoint(mouse_pos):
                draw_rect.y -= 20
                img = pygame.transform.scale(img, (90, 135))

            constantes.PANTALLA.blit(img, draw_rect)

        # mostrar cartas del rival (arriba)
        for i, carta in enumerate(cartas_rival):
            numero, palo = carta
            ruta = "pygame/assets/dorso_cartas/dorso.jpg"
            img = pygame.image.load(ruta)
            img = pygame.transform.scale(img, (80, 120))
            x = 200 + i * 120
            y = 50
            constantes.PANTALLA.blit(img, (x, y))

        pygame.display.flip()




