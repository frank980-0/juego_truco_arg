import pygame
import random
import constantes

def partida(cartas_jugador, cartas_rival):
    corriendo = True
    fondo = pygame.transform.scale(constantes.FONDO, (constantes.ANCHO_PANTALLA, constantes.ALTO_PANTALLA))

    # === CONFIGURACIÓN VISUAL ===
    ancho_carta, alto_carta = 100, 150
    espacio_cartas = 120
    base_jugador_y = constantes.ALTO_PANTALLA - alto_carta - 60
    base_rival_y = 60
    centro_x = constantes.ANCHO_PANTALLA // 2

    # === PREPARAR RECTS JUGADOR ===
    cartas_jugador_rects = []
    inicio_x = centro_x - (len(cartas_jugador) * espacio_cartas // 2)
    for i, carta in enumerate(cartas_jugador):
        x = inicio_x + i * espacio_cartas
        rect = pygame.Rect(x, base_jugador_y, ancho_carta, alto_carta)
        cartas_jugador_rects.append((carta, rect))

    jugadas = []
    carta_jugada_jugador = None
    turno = "jugador"

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

            # click del jugador
            if evento.type == pygame.MOUSEBUTTONDOWN and turno == "jugador":
                mouse_pos = pygame.mouse.get_pos()
                for i, (carta, rect) in enumerate(cartas_jugador_rects):
                    if rect.collidepoint(mouse_pos):
                        carta_jugada_jugador = carta
                        cartas_jugador_rects.pop(i)
                        turno = "rival"
                        break

        # turno del rival (bot)
        if turno == "rival" and carta_jugada_jugador is not None:
            if cartas_rival:
                carta_rival = random.choice(cartas_rival)
                cartas_rival.remove(carta_rival)
                jugadas.append((carta_jugada_jugador, carta_rival))
            carta_jugada_jugador = None
            turno = "jugador"

        # si ambos se quedaron sin cartas, fin
        if not cartas_jugador_rects and not cartas_rival:
            pygame.time.wait(1500)
            corriendo = False

        # === DIBUJAR ===
        constantes.PANTALLA.blit(fondo, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        # Cartas del jugador
        for carta, rect in cartas_jugador_rects:
            numero, palo = carta
            ruta = f"pygame/assets/cartas/{numero}_{palo}.jpg"
            img = pygame.image.load(ruta)
            img = pygame.transform.scale(img, (ancho_carta, alto_carta))

            draw_rect = rect.copy()
            if rect.collidepoint(mouse_pos) and turno == "jugador":
                draw_rect.y -= 20
                img = pygame.transform.scale(img, (int(ancho_carta * 1.1), int(alto_carta * 1.1)))

            constantes.PANTALLA.blit(img, draw_rect)

        # Cartas del rival (dorso)
        inicio_rival_x = centro_x - (len(cartas_rival) * espacio_cartas // 2)
        for i in range(len(cartas_rival)):
            ruta = "pygame/assets/dorso_cartas/dorso.jpg"
            img = pygame.image.load(ruta)
            img = pygame.transform.scale(img, (ancho_carta, alto_carta))
            x = inicio_rival_x + i * espacio_cartas
            y = base_rival_y
            constantes.PANTALLA.blit(img, (x, y))

        # Cartas jugadas al centro
        for i, (cj, cr) in enumerate(jugadas):
            offset_x = -((len(jugadas) - 1) * 70) // 2 + i * 70
            # Jugador
            numj, paloj = cj
            img_j = pygame.image.load(f"pygame/assets/cartas/{numj}_{paloj}.jpg")
            img_j = pygame.transform.scale(img_j, (90, 135))
            constantes.PANTALLA.blit(img_j, (centro_x + offset_x - 45, constantes.ALTO_PANTALLA//2 + 40))
            # Rival
            numr, palor = cr
            img_r = pygame.image.load(f"pygame/assets/cartas/{numr}_{palor}.jpg")
            img_r = pygame.transform.scale(img_r, (90, 135))
            constantes.PANTALLA.blit(img_r, (centro_x + offset_x - 45, constantes.ALTO_PANTALLA//2 - 180))

        pygame.display.flip()
