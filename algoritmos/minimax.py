from distancia_manhattan import distancia_manhattan
from constantes import ARRIBA, ABAJO, IZQUIERDA, DERECHA, ROL
from mover_jugador import mover_jugador

# Función de evaluación
def funcion_evaluacion(pos_maquina, pos_objetivo):
    if pos_maquina == pos_objetivo:
        return -1000
    
    distancia = distancia_manhattan(pos_maquina, pos_objetivo)

    return distancia

# Algoritmo minimax
def minimax(profundidad, rol, pos_maquina, pos_objetivo):
    # Caso base: Llegamos a la profundidad 0 o la Máquina alcanzó su Objetivo
    if profundidad == 0 or pos_maquina == pos_objetivo:
        return funcion_evaluacion(pos_maquina, pos_objetivo)
    
    if rol == ROL[0]: # Rol "Policía"
        mejor_evaluacion = float("inf") # El Policía quiere minimizar
        
        for direccion in [ARRIBA, ABAJO, IZQUIERDA, DERECHA]:
            pos_maquina_temp = pos_maquina.copy() # Copia temporal del policía
            mover_jugador(pos_maquina_temp, direccion) # Simulamos el movimiento
            evaluacion = minimax(profundidad - 1, ROL[1], pos_maquina_temp, pos_objetivo)
            mejor_evaluacion = min(mejor_evaluacion, evaluacion) # Tomamos la mejor evaluación
        return mejor_evaluacion
    else: # Rol "Ladrón"
        mejor_evaluacion = float("-inf") # El Ladrón quiere maximizar
        
        for direccion in [ARRIBA, ABAJO, IZQUIERDA, DERECHA]:
            pos_objetivo_temp = pos_objetivo.copy() # Copia temporal del ladrón
            mover_jugador(pos_objetivo_temp, direccion) # Simulamos el movimiento
            evaluacion = minimax(profundidad - 1, ROL[0], pos_maquina, pos_objetivo_temp)
            mejor_evaluacion = max(mejor_evaluacion, evaluacion) # Tomamos la mejor evaluación
        return mejor_evaluacion