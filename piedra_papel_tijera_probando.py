import random
from constants import JUGADOR, PASOS, ROL, OPCIONES

def obtener_eleccion_usuario(rol):
    eleccion = input(f"\n- ({"Policía" if rol == ROL[0] else "Ladrón"}) Elige piedra, papel o tijera: ").lower()
    while eleccion not in OPCIONES:
        print("Elección no válida. Intenta de nuevo.")
        eleccion = input(f"\n- ({rol}) Elige piedra, papel o tijera: ").lower()
    
    return eleccion

def obtener_eleccion_computadora():
    return random.choice(OPCIONES)

def determinar_ganador(eleccion_usuario, eleccion_computadora):
    if eleccion_usuario == eleccion_computadora:
        print("\n\t\tEMPATE")
        return "Empate"
    elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or \
        (eleccion_usuario == "tijera" and eleccion_computadora == "papel") or \
        (eleccion_usuario == "papel" and eleccion_computadora == "piedra"):
        print("\n\t\tHAS GANADO")
        return JUGADOR["u"], PASOS[eleccion_usuario], eleccion_usuario
    else:
        print("\n\t\tHA GANADO LA COMPUTADORA")
        return JUGADOR["c"], PASOS[eleccion_computadora], eleccion_computadora

def piedra_papel_tijera(rol):
    print("\n\t\t\tPIEDRA, PAPEL O TIJERA")
    
    while True:
        eleccion_usuario = obtener_eleccion_usuario(rol)
        eleccion_computadora = obtener_eleccion_computadora()
        
        print(f"\n\t- Tú elegiste: {eleccion_usuario}")
        print(f"\t- La computadora eligió: {eleccion_computadora}")
        
        resultado = determinar_ganador(eleccion_usuario, eleccion_computadora)
        
        if resultado != "Empate": break
    
    return resultado