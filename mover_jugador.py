from constantes import ARRIBA, ABAJO, IZQUIERDA, DERECHA, FILAS, COLUMNAS

def mover_jugador(jugador, direccion):
    if direccion == ARRIBA and jugador[0] > 0:  # Arriba
        jugador[0] -= 1
        return True
    elif direccion == ABAJO and jugador[0] < FILAS - 1:  # Abajo
        jugador[0] += 1
        return True
    elif direccion == IZQUIERDA and jugador[1] > 0:  # Izquierda
        jugador[1] -= 1
        return True
    elif direccion == DERECHA and jugador[1] < COLUMNAS - 1:  # Derecha
        jugador[1] += 1
        return True
    else:
        return False