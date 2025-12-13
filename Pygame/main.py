import pygame
from gui import menu, pedir_nombre,salir, ranking,partida_grafica
from logica import persistencias, cartas, ganador
import constantes

pygame.init() 

opcion = menu.mostrar_menu()

if opcion == "jugar":
    print("Iniciando juego...")
    nombre  = pedir_nombre.pedir_nombre(constantes.PANTALLA)
    print(f"Nombre del jugador: {nombre}")
    cartas_jugador, cartas_rival = cartas.repartir_cartas()
    jugadas =partida_grafica.partida(cartas_jugador, cartas_rival)
    ganador = ganador.ganador_partida(jugadas)
    print(f"El ganador de la partida es: {ganador}")
# Por ahora guardamos la partida como si siempre ganara el jugador
    persistencias.guardar_partida(nombre, "CPU", ganador="CPU")
elif opcion == "salir":

    salir.mostrar_salir(constantes.PANTALLA)
elif opcion == "ranking":
    ranking.mostrar_ranking(constantes.PANTALLA)
    print("Mostrando ranking...")

pygame.quit() 