import os, msvcrt, random
from piedra_papel_tijera_probando import piedra_papel_tijera
from constants import TABLERO, JUGADOR

# Dimensiones del tablero
filas, columnas = TABLERO

# Posiciones iniciales de los jugadores
jugador1 = [0, 0]  # Esquina superior izquierda
jugador2 = [filas - 1, columnas - 1]  # Esquina inferior derecha

def imprimir_tablero():
    for i in range(filas):
        for j in range(columnas):
            if [i, j] == jugador1:
                print("1", end=" ")
            elif [i, j] == jugador2:
                print("2", end=" ")
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

def mostrar_datos_turno(turno, pasos, opcion, cont_turnos):
    print(f"\n\t\tPOLICÍA VS LADRÓN -> Turno N°{cont_turnos}")
    print(f"\n- Turno: {turno}\n- Opción escogida: {opcion}\n- Pasos obtenidos: {pasos}\n")
    
    
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
    
cont_turnos = 1

# Empezamos el juego
while True:
    # Juego por turnos
    turno, pasos, opcion = piedra_papel_tijera()
    
    # time.sleep(3)
    msvcrt.getch()
    
    os.system("cls")
    
    mostrar_datos_turno(turno, pasos, opcion, cont_turnos)
    
    imprimir_tablero()
    
    pasos_disponibles = pasos
    
    if turno == JUGADOR["u"]:
        while pasos_disponibles > 0:
            print(f"\nPasos disponibles: {pasos_disponibles}")
            movimiento = input("\nUsuario (WASD): ").lower()
            mover_jugador(jugador1, movimiento)
            pasos_disponibles -= 1
            
            os.system("cls")
            
            mostrar_datos_turno(turno, pasos, opcion, cont_turnos)
            
            imprimir_tablero()
        
    else:
        while pasos_disponibles > 0:
            print(f"\nPasos disponibles: {pasos_disponibles}")
            movimiento = input("\nComputadora (WASD): ").lower()
            # Acá en sí debemos hacer que la PC se mueva por sí sola
            mover_jugador(jugador2, movimiento)
            pasos_disponibles -= 1
            
            os.system("cls")
            
            mostrar_datos_turno(turno, pasos, opcion, cont_turnos)
            
            imprimir_tablero()
    
    cont_turnos += 1
