import constantes
def generar_cartas():
# generamos las cartas,palos, y valores de las cartas

    palos = constantes.PALOS
    numeros = constantes.NUMEROS            

    cartas = []
# se genera una lista vacia y recorremos las tuplas de palos y numeros
# y la agregamos a la lista de cartas

    for palo in palos:
        for numero in numeros:
            cartas.append((numero, palo))

    return cartas




