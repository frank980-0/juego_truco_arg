import pygame
from gui import menu, pedir_nombre, cartas_graficas,salir, ranking,partida_grafica
from logica.cartas import repartir_cartas
import constantes

pygame.init() 

opcion = menu.mostrar_menu()

if opcion == "jugar":
    print("Iniciando juego...")
    nombre  = pedir_nombre.pedir_nombre(constantes.PANTALLA)
    print(f"Nombre del jugador: {nombre}")
    cartas_jugador, cartas_rival = repartir_cartas()
    partida_grafica.partida(cartas_jugador, cartas_rival)
    
# Por ahora guardamos la partida como si siempre ganara el jugador
    ranking.guardar_partida(nombre, "CPU", ganador="CPU")

elif opcion == "salir":

    salir.mostrar_salir(constantes.PANTALLA)
elif opcion == "ranking":
    ranking.mostrar_ranking(constantes.PANTALLA)
    print("Mostrando ranking...")

pygame.quit() 