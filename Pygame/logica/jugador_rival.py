# oponente tira una carta al azar de su mano
import random

def jugar_carta_rival(cartas_rival :list):
    if cartas_rival:
        carta_rival = random.choice(cartas_rival)
        cartas_rival.remove(carta_rival)
        return carta_rival
    return None
