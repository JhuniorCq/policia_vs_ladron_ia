import os, msvcrt, random
from piedra_papel_tijera_probando import piedra_papel_tijera
from constants import TABLERO, JUGADOR, ROL, CANTIDAD_CASAS

# Dimensiones del tablero
filas, columnas = TABLERO

# Posiciones iniciales de los jugadores
posicion_policia = [0, 0]  # Esquina superior izquierda / Policía
posicion_ladron = [filas - 1, columnas - 1]  # Esquina inferior derecha / Ladrón

def imprimir_tablero():
    for i in range(filas):
        for j in range(columnas):
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
    if direccion == "w" and jugador[0] > 0:  # Arriba
        jugador[0] -= 1
    elif direccion == "s" and jugador[0] < filas - 1:  # Abajo
        jugador[0] += 1
    elif direccion == "a" and jugador[1] > 0:  # Izquierda
        jugador[1] -= 1
    elif direccion == "d" and jugador[1] < columnas - 1:  # Derecha
        jugador[1] += 1

##################
def realizar_pasos():
    pass

def mostrar_datos_turno(turno, pasos, opcion, cont_turnos, rol):
    print(f"\n\t\tPOLICÍA VS LADRÓN -> Turno N°{cont_turnos}")
    print(f"\n- Turno: {turno}\n- Opción escogida: {opcion}\n- Pasos obtenidos: {pasos}\n- Rol: {"Policía" if rol == ROL[0] else "Ladrón"}")
    if rol == ROL[1]:
        print(f"- Casas robadas: {posiciones_casas_robadas}\n")
    
    
######## FUNCIONES PARA LAS CASAS
# Función para calcular la distancia de Manhattan entre dos puntos
def distancia_separacion(casa1, casa2):
    return abs(casa1[0] - casa2[0]) + abs(casa1[1] - casa2[1])

# Función para generar posiciones de las casitas
def generar_posiciones_casa():
    casas = []
    
    while len(casas) < CANTIDAD_CASAS:
        # Generar una posición aleatoria
        nueva_casa = [random.randint(0, filas-1), random.randint(0, columnas-1)]
        
        # Verificar que la nueva casita esté al menos a 5 casillas de Manhattan de las demás
        if all(distancia_separacion(nueva_casa, casa) >= 5 for casa in casas) and nueva_casa != [0,0] and nueva_casa != [24,19]:
            casas.append(nueva_casa)
    
    return casas

posiciones_casas = generar_posiciones_casa()
########

def obtener_roles():
    print("\n\t\tESCOGE TU ROL")
    rol_usuario = input("\n- Para ser policía escribe (p) y para ser ladrón escribe (l): ").lower()
    
    while rol_usuario not in ROL:
        print("\n\tElección no válida. Intenta de nuevo.")
        rol_usuario = input("\n- Para ser policía escribe (p) y para ser ladrón escribe (l): ").lower()
        
    rol_computadora = ROL[1] if rol_usuario == ROL[0] else ROL[0]
    
    return rol_usuario, rol_computadora

cont_turnos = 1
posiciones_casas_robadas = []

# Empezamos el juego

# Acá se le debe preguntar al usuario que rol quiere ser
rol_usuario, rol_computadora = obtener_roles()

juego_en_curso = True

while juego_en_curso:
    # Juego por turnos
    turno, pasos, opcion = piedra_papel_tijera(rol_usuario)
    
    # time.sleep(3)
    msvcrt.getch()
    
    os.system("cls")
    
    # Acá podemos agregar el rol
    mostrar_datos_turno(turno, pasos, opcion, cont_turnos, rol_usuario if turno == JUGADOR["u"] else rol_computadora)
    
    imprimir_tablero()
    
    pasos_disponibles = pasos
    
    if turno == JUGADOR["u"]:
        while pasos_disponibles > 0:
            print(f"\nPasos disponibles: {pasos_disponibles}")
            movimiento = input("\nUsuario (WASD): ").lower()
            mover_jugador(posicion_policia if rol_usuario == ROL[0] else posicion_ladron, movimiento)
            pasos_disponibles -= 1
            
            os.system("cls")
            mostrar_datos_turno(turno, pasos, opcion, cont_turnos, rol_usuario)
            imprimir_tablero()
        
        
        if rol_usuario == ROL[0]: # Policía
            if posicion_policia == posicion_ladron: 
                print("\n\t\tEL POLICÍA HA ATRAPADO AL LADRÓN. HA GANADO EL POLICÍA.\n")
                msvcrt.getch()
                juego_en_curso = False
        else: # Ladrón
            if posicion_ladron in posiciones_casas:
                print(f"\n\t\tSe ha robado una casa en {posicion_ladron}.")
                
                casa_robada = posicion_ladron.copy()
                posiciones_casas_robadas.append(casa_robada)

                msvcrt.getch()
                
                if len(posiciones_casas_robadas) == CANTIDAD_CASAS:
                    print("\n\t\tSE HAN ROBADO TODAS LAS CASAS. HA GANADO EL LADRÓN.\n")
                    juego_en_curso = False
        
    else:
        while pasos_disponibles > 0:
            print(f"\nPasos disponibles: {pasos_disponibles}")
            movimiento = input("\nComputadora (WASD): ").lower()
            # Acá en sí debemos hacer que la PC se mueva por sí sola
            mover_jugador(posicion_ladron if rol_computadora == ROL[1] else posicion_policia, movimiento)
            pasos_disponibles -= 1
            
            os.system("cls")
            mostrar_datos_turno(turno, pasos, opcion, cont_turnos, rol_computadora)
            imprimir_tablero()

        if rol_computadora == ROL[0]: # Policía
            if posicion_policia == posicion_ladron:
                print("\n\t\tEL POLICÍA HA ATRAPADO AL LADRÓN. HA GANADO EL POLICÍA.\n")
                msvcrt.getch()
                juego_en_curso = False
        else: # Ladrón
            if posicion_ladron in posiciones_casas:
                print(f"\n\t\tSe ha robado una casa en {posicion_ladron}.")
                
                casa_robada = posicion_ladron.copy()
                posiciones_casas_robadas.append(casa_robada)

                msvcrt.getch()
                
                if len(posiciones_casas_robadas) == CANTIDAD_CASAS:
                    print("\n\t\tSE HAN ROBADO TODAS LAS CASAS. HA GANADO EL LADRÓN.\n")
                    juego_en_curso = False
    
    cont_turnos += 1