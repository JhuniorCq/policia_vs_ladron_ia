from distancia_manhattan import distancia_manhattan
from constantes import ARRIBA, ABAJO, IZQUIERDA, DERECHA, ROL
from mover_jugador import mover_jugador

# Función de evaluación -> Creo que acá no más cambiará para el ladrón
def funcion_evaluacion(pos_maquina, pos_objetivo):
    # Si el policía atrapa al ladrón, devolvemos un puntaje muy bajo (victoria del policía)
    if pos_maquina == pos_objetivo:
        return -1000
    
    # Calculamos la distancia Manhattan entre el policía y el ladrón
    distancia = distancia_manhattan(pos_maquina, pos_objetivo)

    # Si el ladrón aún está libre, devolvemos la distancia como evaluación
    return distancia  # Queremos minimizar la distancia entre ellos

# Algoritmo minimax
def minimax(profundidad, rol, pos_maquina, pos_objetivo):
    # Caso base: Llegamos a la profundidad 0 o el Policiía atrapó al ladrón
    if profundidad == 0 or pos_maquina == pos_objetivo:
        return funcion_evaluacion(pos_maquina, pos_objetivo) # Se evalúa la situación actual
    
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