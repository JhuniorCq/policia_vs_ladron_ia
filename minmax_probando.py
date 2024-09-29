import random, os

# Dimensiones del tablero
filas = 25
columnas = 20

# Posiciones iniciales
posicion_policia = [0, 0]
posicion_ladron = [24, 19]

# Constantes para los movimientos
ARRIBA = "arriba"
ABAJO = "abajo"
IZQUIERDA = "izquierda"
DERECHA = "derecha"

# Función para imprimir el tablero
def imprimir_tablero():
    for i in range(filas):
        for j in range(columnas):
            if [i, j] == posicion_policia:
                print("P", end=" ")
            elif [i, j] == posicion_ladron:
                print("L", end=" ")
            else:
                print(".", end=" ")
        print()

# Función para mover jugador en el tablero un solo paso
def mover_jugador(jugador, direccion):
    if direccion == ARRIBA and jugador[0] > 0:
        jugador[0] -= 1
    elif direccion == ABAJO and jugador[0] < filas - 1:
        jugador[0] += 1
    elif direccion == IZQUIERDA and jugador[1] > 0:
        jugador[1] -= 1
    elif direccion == DERECHA and jugador[1] < columnas - 1:
        jugador[1] += 1

# Función para calcular la distancia de Manhattan
def distancia_manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

# Función minimax adaptada a pasos por turno
def minimax(profundidad, es_turno_policia, pasos_restantes, pos_policia, pos_ladron):
    # Caso base: alcanzamos la profundidad o el policía atrapó al ladrón
    if profundidad == 0 or pos_policia == pos_ladron:
        return funcion_evaluacion(pos_policia, pos_ladron)  # Evaluamos la situación actual
    
    if es_turno_policia:
        mejor_evaluacion = float('inf')  # Queremos minimizar (mejor para el policía)
        for direccion in [ARRIBA, ABAJO, IZQUIERDA, DERECHA]:
            pos_policia_temp = pos_policia.copy()  # Copia temporal del policía
            mover_jugador(pos_policia_temp, direccion)  # Simulamos el movimiento
            evaluacion = minimax(profundidad - 1, False, pasos_restantes, pos_policia_temp, pos_ladron)
            mejor_evaluacion = min(mejor_evaluacion, evaluacion)  # Tomamos la mejor evaluación (mínima)
        return mejor_evaluacion
    else:
        mejor_evaluacion = float('-inf')  # Queremos maximizar (mejor para el ladrón)
        for direccion in [ARRIBA, ABAJO, IZQUIERDA, DERECHA]:
            pos_ladron_temp = pos_ladron.copy()  # Copia temporal del ladrón
            mover_jugador(pos_ladron_temp, direccion)  # Simulamos el movimiento
            evaluacion = minimax(profundidad - 1, True, pasos_restantes, pos_policia, pos_ladron_temp)
            mejor_evaluacion = max(mejor_evaluacion, evaluacion)  # Tomamos la mejor evaluación (máxima)
        return mejor_evaluacion

# TODO: Lo que faltaría es que en "minimax", la función "funcion_evaluación()" EVALUÉ las posiciones futuras del ladrón y el policiía, ya que cada iteración dentro de "minimax" es una posible situación futura

# Función de evaluación
def funcion_evaluacion(pos_policia, pos_ladron):
    # Calculamos la distancia Manhattan entre el policía y el ladrón
    distancia = distancia_manhattan(pos_policia, pos_ladron)

    # Si el policía atrapa al ladrón, devolvemos un puntaje muy bajo (victoria del policía)
    if pos_policia == pos_ladron:
        return -1000  # Victoria para el policía

    # Si el ladrón aún está libre, devolvemos la distancia como evaluación
    return distancia  # Queremos minimizar la distancia entre ellos

# Simulación de movimiento de la computadora (policía)
def movimiento_policia(pasos):
    for _ in range(pasos):  # Iteramos por cada paso que tiene permitido
        mejor_evaluacion = float('inf')  # Queremos minimizar la distancia al ladrón
        mejor_movimiento = None

        # Probar cada dirección posible
        for direccion in [ARRIBA, ABAJO, IZQUIERDA, DERECHA]:
            posicion_policia_temp = posicion_policia.copy()  # Hacemos una copia temporal
            mover_jugador(posicion_policia_temp, direccion)  # Simulamos mover en esa dirección

            # Evaluamos la jugada usando Minimax
            evaluacion = minimax(3, False, pasos - 1, posicion_policia_temp, posicion_ladron.copy()) 
            # Si la evaluación es mejor, actualizamos el mejor movimiento
            if evaluacion < mejor_evaluacion:
                mejor_evaluacion = evaluacion
                mejor_movimiento = direccion

        # Ejecutar el mejor movimiento en la posición real del policía
        mover_jugador(posicion_policia, mejor_movimiento)

        # Mostrar el movimiento en consola
        print(f"Policía se mueve {mejor_movimiento}")
        imprimir_tablero()

# Simulación de movimiento del jugador humano (ladrón)
def movimiento_ladron(pasos):
    for _ in range(pasos):
        direccion = input("Elige la dirección del ladrón (arriba, abajo, izquierda, derecha): ")
        mover_jugador(posicion_ladron, direccion)
        os.system("cls")
        print(f"Ladrón se mueve {direccion}")
        imprimir_tablero()

# Función para simular el juego
def jugar():
    turno = 0  # 0: policía, 1: ladrón
    while posicion_policia != posicion_ladron:
        imprimir_tablero()
        pasos = random.randint(1, 6)  # Determinar pasos al azar para cada jugador
        if turno == 0:
            print(f"Turno de la policía. Pasos: {pasos}")
            movimiento_policia(pasos)
        else:
            print(f"Turno del ladrón. Pasos: {pasos}")
            movimiento_ladron(pasos)
        
        turno = 1 - turno  # Cambia el turno

# Ejecución del juego
jugar()
