import pygame
from assets import *
from gui import menu, pedir_nombre, cartas_graficas,salir
from logica.jugador_rival import repartir_cartas
import constantes
pygame.init() #inicializa los recursos de Pygame

opcion = menu.mostrar_menu()

if opcion == "jugar":
    print("Iniciando juego...")
    nombre  = pedir_nombre.pedir_nombre(constantes.PANTALLA)
    print(f"Nombre del jugador: {nombre}")
    cartas_jugador, cartas_rival = repartir_cartas()
    cartas_graficas.mostrar_mano(cartas_jugador, cartas_rival)

elif opcion == "salir":
    salir.mostrar_salir(constantes.PANTALLA)
elif opcion == "ranking":
    print("Mostrando ranking...")

pygame.quit() #finaliza los recursos de Pygame