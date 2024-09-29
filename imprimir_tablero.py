from constantes import FILAS, COLUMNAS

def imprimir_tablero(pos_policia, pos_ladron, pos_casas,pos_casas_robadas):
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if [i, j] == pos_policia:
                print("P", end=" ")
            elif [i, j] == pos_ladron:
                print("L", end=" ")
            elif [i, j] in pos_casas_robadas:
                print("X", end=" ")
            elif [i, j] in pos_casas:
                print("C", end=" ")
            else:
                print(".", end=" ")
        print()