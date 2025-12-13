import pygame
'''archivo de constantes globales'''

# dimensiones de la pantalla
ANCHO_PANTALLA = 900
ALTO_PANTALLA = 700

PANTALLA = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA)) #crea una ventana de 800x600 píxeles
FONDO = pygame.image.load("pygame/assets/fondo/mesa.jpg")
FAVICON = pygame.image.load("pygame/assets/favicon/icono.jpg")
RUTA_CARTA = f"pygame/assets/cartas/{{numero}}_{{palo}}.jpg"


# colores de texto
BLANCO = (255, 255, 255)
NEGRO  = (0, 0, 0)
ROJO   = (255, 0, 0)
VERDE  = (0, 187, 45)
AZUL   = (0, 0, 255)

# Tupla de las cartas
PALOS = ("copa","oro","basto","espada")
NUMEROS = (1,2,3,4,5,6,7,10,11,12)

# jerarquia de las cartas para comparar
VALORES = {
        (1, "espada"): 14,
        (1, "basto"): 13,
        (7, "espada"): 12,
        (7, "oro"): 11,
        (3, ""): 10,  # cualquier 3
        (2, ""): 9,
        (1, ""): 8,   # 1 de copa u oro
        (12, ""): 7,
        (11, ""): 6,
        (10, ""): 5,
        (7, ""): 4,
        (6, ""): 3,
        (5, ""): 2,
        (4, ""): 1
    }