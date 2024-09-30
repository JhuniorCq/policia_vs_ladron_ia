from distancia_manhattan import distancia_manhattan
from constantes import ARRIBA, ABAJO, IZQUIERDA, DERECHA, ROL
from mover_jugador import mover_jugador

# Función de evaluación
def funcion_evaluacion(pos_policia, pos_ladron):
    # Si el policía atrapa al ladrón, devolvemos un puntaje muy bajo (victoria del policía)
    if pos_policia == pos_ladron:
        return -1000  # Victoria para el policía
    
    # Calculamos la distancia Manhattan entre el policía y el ladrón
    distancia = distancia_manhattan(pos_policia, pos_ladron)

    # Si el ladrón aún está libre, devolvemos la distancia como evaluación
    return distancia  # Queremos minimizar la distancia entre ellos

# Algoritmo minimax
def minimax(profundidad, rol, pos_policia, pos_ladron):
    # Caso base: Llegamos a la profundidad 0 o el Policiía atrapó al ladrón
    if profundidad == 0 or pos_policia == pos_ladron:
        return funcion_evaluacion(pos_policia, pos_ladron) # Se evalúa la situación actual
    
    if rol == ROL[0]:
        mejor_evaluacion = float("inf") # El Policía quiere minimizar
        
        for direccion in [ARRIBA, ABAJO, IZQUIERDA, DERECHA]:
            pos_policia_temp = pos_policia.copy() # Copia temporal del policía
            mover_jugador(pos_policia_temp, direccion) # Simulamos el movimiento
            evaluacion = minimax(profundidad - 1, False, pos_policia_temp, pos_ladron)
            mejor_evaluacion = min(mejor_evaluacion, evaluacion) # Tomamos la mejor evaluación
        return mejor_evaluacion
    else:
        mejor_evaluacion = float("-inf") # El Ladrón quiere maximizar
        
        for direccion in [ARRIBA, ABAJO, IZQUIERDA, DERECHA]:
            pos_ladron_temp = pos_ladron.copy() # Copia temporal del ladrón
            mover_jugador(pos_ladron_temp, direccion) # Simulamos el movimiento
            evaluacion = minimax(profundidad - 1, True, pos_policia, pos_ladron_temp)
            mejor_evaluacion = max(mejor_evaluacion, evaluacion) # Tomamos la mejor evaluación
        return mejor_evaluacion