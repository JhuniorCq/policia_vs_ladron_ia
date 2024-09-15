import os, msvcrt, random
from piedra_papel_tijera_probando import piedra_papel_tijera
from constants import TABLERO, JUGADOR, SIMBOLO_ROL

# Dimensiones del tablero
filas, columnas = TABLERO

# Posiciones iniciales de los jugadores
jugador1 = [0, 0]  # Esquina superior izquierda / Policía
jugador2 = [filas - 1, columnas - 1]  # Esquina inferior derecha / Ladrón

def imprimir_tablero():
    for i in range(filas):
        for j in range(columnas):
            if [i, j] == jugador1:
                print("P", end=" ")
            elif [i, j] == jugador2:
                print("L", end=" ")
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
    print(f"\n- Turno: {turno}\n- Opción escogida: {opcion}\n- Pasos obtenidos: {pasos}\n- Rol: {"Policía" if rol == SIMBOLO_ROL[0] else "Ladrón"}\n")
    
    
######## FUNCIONES PARA LAS CASAS
# Función para calcular la distancia de Manhattan entre dos puntos
def distancia_separacion(casa1, casa2):
    return abs(casa1[0] - casa2[0]) + abs(casa1[1] - casa2[1])

# Función para generar posiciones de las casitas
def generar_posiciones_casa():
    casas = []
    
    while len(casas) < 7:
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
    
    while rol_usuario not in SIMBOLO_ROL:
        print("Elección no válida. Intenta de nuevo.")
        rol_usuario = input("\n- Para ser policía escribe (p) y para ser ladrón escribe (l): ").lower()
        
    rol_computadora = SIMBOLO_ROL[1] if rol_usuario == SIMBOLO_ROL[0] else SIMBOLO_ROL[0]
    
    return rol_usuario, rol_computadora

cont_turnos = 1

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
            mover_jugador(jugador1 if rol_usuario == SIMBOLO_ROL[0] else jugador2, movimiento)
            pasos_disponibles -= 1
            
            os.system("cls")
            
            mostrar_datos_turno(turno, pasos, opcion, cont_turnos, rol_usuario)
            
            imprimir_tablero()
        
        # Policía
        if rol_usuario == SIMBOLO_ROL[0]:
            # Policía y ladrón deben tener la misma posición, en el último paso del policía
            if jugador1 == jugador2: 
                print("\n\t\tEl policía ha atrapado al ladrón.")
                msvcrt.getch()
                juego_en_curso = False
        # Ladrón
        else:
            if jugador2 in posiciones_casas:
                print("\n\t\tSe ha robado una casa.")
                msvcrt.getch()
        
    else:
        while pasos_disponibles > 0:
            print(f"\nPasos disponibles: {pasos_disponibles}")
            movimiento = input("\nComputadora (WASD): ").lower()
            # Acá en sí debemos hacer que la PC se mueva por sí sola
            mover_jugador(jugador2 if rol_computadora == SIMBOLO_ROL[1] else jugador1, movimiento)
            pasos_disponibles -= 1
            
            os.system("cls")
            
            mostrar_datos_turno(turno, pasos, opcion, cont_turnos, rol_computadora)
            
            imprimir_tablero()
    
    cont_turnos += 1


# TODO: Falta hacer lo que hará la PC cuando sea policía o ladrón (en el Usuario ya está avanzado gran parte)
# TODO: Hacer que cuando el ladrón robe una casa, la casa se marque con X