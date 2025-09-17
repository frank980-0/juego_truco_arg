import constantes
import pygame

# def cargar_cartas():
#     palos = constantes.PALOS
#     numeros = constantes.NUMEROS

#     cartas = []
#     for palo in palos:
#         for numero in numeros:
#             ruta = f"pygame/assets/cartas/{numero}_{palo}.jpg"
#             imagenes = pygame.image.load(ruta)
#             imagenes = pygame.transform.scale(imagenes, (80, 120))
#             cartas.append(imagenes)
    
#     corriendo = True

#     while corriendo:

#         fondo = pygame.transform.scale(constantes.FONDO, (constantes.ANCHO_PANTALLA, constantes.ALTO_PANTALLA)) #carga y redimensiona la imagen de fondo
#         for evento in pygame.event.get():
#             if evento.type == pygame.QUIT:
#                 corriendo = False

#         constantes.PANTALLA.blit(fondo, (0, 0))

#     # Dibujar las primeras 5 cartas como ejemplo
#         for i, carta in enumerate(cartas[:5]):
#             x = 50 + i * 100
#             y = 200
#             constantes.PANTALLA.blit(carta, (x, y))

#         pygame.display.flip()


def mostrar_mano(cartas_jugador, cartas_rival):
    """Dibuja las cartas del jugador y del rival en pantalla"""
    corriendo = True
    # cargar fondo
    fondo = pygame.transform.scale(constantes.FONDO, (constantes.ANCHO_PANTALLA, constantes.ALTO_PANTALLA))

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        # dibujar fondo
        constantes.PANTALLA.blit(fondo, (0, 0))

        # mostrar cartas del jugador (abajo)
        for i, carta in enumerate(cartas_jugador):
            numero, palo = carta
            ruta = f"pygame/assets/cartas/{numero}_{palo}.jpg"
            img = pygame.image.load(ruta)
            img = pygame.transform.scale(img, (80, 120))
            x = 200 + i * 120
            y = 400
            constantes.PANTALLA.blit(img, (x, y))

        # mostrar cartas del rival (arriba)
        for i, carta in enumerate(cartas_rival):
            numero, palo = carta
            ruta = f"pygame/assets/cartas/{numero}_{palo}.jpg"
            img = pygame.image.load(ruta)
            img = pygame.transform.scale(img, (80, 120))
            x = 200 + i * 120
            y = 50
            constantes.PANTALLA.blit(img, (x, y))

        pygame.display.flip()




