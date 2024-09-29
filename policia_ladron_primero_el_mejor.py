import os, msvcrt, random, heapq, time
from constants import TABLERO, JUGADOR, ROL, CANTIDAD_CASAS, ARRIBA, ABAJO, DERECHA, IZQUIERDA, VALORES_DADO, FILAS, COLUMNAS
from distancia_manhattan import distancia_manhattan
from algoritmos.primero_el_mejor import movimiento_mejor_primero

def imprimir_tablero():
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if [i, j] == posicion_policia:
                print("P", end=" ")
            elif [i, j] == posicion_ladron:
                print("L", end=" ")
            elif [i, j] in posiciones_casas_robadas:
                print("X", end=" ")
            elif [i, j] in posiciones_casas:
                print("C", end=" ")
            else:
                print(".", end=" ")
        print()

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

def generar_posiciones_casa():
    casas = []
    
    while len(casas) < CANTIDAD_CASAS:
        # Generar una posición aleatoria
        nueva_casa = [random.randint(0, FILAS-1), random.randint(0, COLUMNAS-1)]
        
        # Verificar que la nueva casita esté al menos a 5 casillas de Manhattan de las demás
        if all(distancia_manhattan(nueva_casa, casa) >= 5 for casa in casas) and nueva_casa != [0,0] and nueva_casa != [24,19]:
            casas.append(nueva_casa)
    
    return casas

def mostrar_datos_turno(turno, pasos, cont_turnos, rol): 
    print(f"\n\t\tPOLICÍA VS LADRÓN -> Turno N°{cont_turnos}")
    print(f"\n- Turno: {turno}\n- Pasos obtenidos: {pasos}\n- Rol: {"Policía" if rol == ROL[0] else "Ladrón"}")
    if rol == ROL[1]:
        print(f"- Casas robadas: {posiciones_casas_robadas}\n")

def obtener_roles():
    print("\n\t\tESCOGE TU ROL")
    rol_usuario = input("\n- Para ser policía escribe (p) y para ser ladrón escribe (l): ").lower()
    
    while rol_usuario not in ROL:
        print("\n\tElección no válida. Intenta de nuevo.")
        rol_usuario = input("\n- Para ser policía escribe (p) y para ser ladrón escribe (l): ").lower()
        
    rol_computadora = ROL[1] if rol_usuario == ROL[0] else ROL[0]
    
    return rol_usuario, rol_computadora

def definir_turno_inicial():
    return random.choice(list(JUGADOR.values()))

def lanzar_dado():
    return random.choice(VALORES_DADO)

# Posiciones iniciales de los jugadores
posicion_policia = [0, 0]
posicion_ladron = [FILAS - 1, COLUMNAS - 1] 

# Contador de turnos
cont_turnos = 1

# Lista con las posiciones de las casas
posiciones_casas = generar_posiciones_casa()

# Lista para las posiciones de las casas robadas
posiciones_casas_robadas = []

############ Empezamos el juego ############

# Indicador del inicio del juego
juego_en_curso = True

# Obtención de roles
rol_usuario, rol_computadora = obtener_roles()
turno = definir_turno_inicial()

while juego_en_curso:
    # Lanzar dado
    print(f"\n\t\tLANZAR EL DADO (Turno: {turno})")
    pasos = lanzar_dado()
    
    print(f"\n\t- Pasos obtenidos: {pasos}")
    msvcrt.getch()
    os.system("cls")
    
    mostrar_datos_turno(turno, pasos, cont_turnos, rol_usuario if turno == JUGADOR["u"] else rol_computadora)
    imprimir_tablero()
    
    pasos_disponibles = pasos
    
    if turno == JUGADOR["u"]:
        # Realizar pasos
        while pasos_disponibles > 0:
            print(f"\nPasos disponibles: {pasos_disponibles}")
            movimiento = input("\nUsuario (WASD): ").lower()
            movida_valida = mover_jugador(posicion_policia if rol_usuario == ROL[0] else posicion_ladron, movimiento)
            
            if movida_valida:
                pasos_disponibles -= 1
            
            os.system("cls")
            mostrar_datos_turno(turno, pasos, cont_turnos, rol_usuario)
            imprimir_tablero()
        else:
            print("\n\t\tPASOS TERMINADOS")
        
        # Rol "Policía"
        if rol_usuario == ROL[0]:
            if posicion_policia == posicion_ladron:
                print("\n\t\tEL POLICÍA HA ATRAPADO AL LADRÓN. HA GANADO EL POLICÍA.\n")
                juego_en_curso = False
        else: # Rol "Ladrón"
            if (posicion_ladron in posiciones_casas) and (posicion_ladron not in posiciones_casas_robadas):
                print(f"\n\t\tSe ha robado una casa en {posicion_ladron}.")
                
                casa_robada = posicion_ladron.copy()
                posiciones_casas_robadas.append(casa_robada)
                
                if len(posiciones_casas_robadas) == CANTIDAD_CASAS:
                    print("\n\t\tSE HAN ROBADO TODAS LAS CASAS. HA GANADO EL LADRÓN.\n")
                    juego_en_curso = False
    else:
        while pasos_disponibles > 0:
            print(f"\nPasos disponibles: {pasos_disponibles}")
            
            # Rol "Policía"
            if rol_computadora == ROL[0]:
                # Uso del algoritmo Primero el Mejor para econtrar el mejor movimiento
                nueva_posicion = movimiento_mejor_primero(posicion_policia, posicion_ladron, rol_computadora, posicion_policia, posicion_ladron)
                posicion_policia = nueva_posicion
            else: # Rol "Ladrón"
                distancia_casas = []
                # Obtenemos la casa más cercana al ladrón
                for posicion_casa in posiciones_casas:
                    if posicion_casa in posiciones_casas_robadas:
                        continue
                        
                    distancia_casa = distancia_manhattan(posicion_ladron, posicion_casa)
                    heapq.heappush(distancia_casas, (distancia_casa, posicion_casa))
                    
                posicion_casa_cercana = heapq.heappop(distancia_casas)
                
                # Movimiento del ladrón a la casa más cercana
                nueva_posicion = movimiento_mejor_primero(posicion_ladron, posicion_casa_cercana[1], rol_computadora, posicion_policia, posicion_ladron)
                posicion_ladron = nueva_posicion
            
            pasos_disponibles -= 1
            
            time.sleep(0.5)
            
            os.system("cls")
            mostrar_datos_turno(turno, pasos, cont_turnos, rol_computadora)
            imprimir_tablero()
        else:
            print("\n\t\tPASOS TERMINADOS")

        # Rol "Policía"
        if rol_computadora == ROL[0]:
            if posicion_policia == posicion_ladron:
                print("\n\t\tEL POLICÍA HA ATRAPADO AL LADRÓN. HA GANADO EL POLICÍA.\n")
                juego_en_curso = False
        else: # Rol "Ladrón"
            if posicion_ladron in posiciones_casas and posicion_ladron not in posiciones_casas_robadas:
                print(f"\n\t\tSe ha robado una casa en {posicion_ladron}.")
                
                casa_robada = posicion_ladron.copy()
                posiciones_casas_robadas.append(casa_robada)

                if len(posiciones_casas_robadas) == CANTIDAD_CASAS:
                    print("\n\t\tSE HAN ROBADO TODAS LAS CASAS. HA GANADO EL LADRÓN.\n")
                    juego_en_curso = False
    
    # Cambiar turno
    turno = JUGADOR["u"] if turno == JUGADOR["c"] else JUGADOR["c"]
    
    # Aumentar el contador de turnos
    cont_turnos += 1
    msvcrt.getch()
