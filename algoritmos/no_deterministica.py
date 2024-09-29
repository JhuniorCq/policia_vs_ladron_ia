import random
from constantes import ARRIBA, ABAJO, IZQUIERDA, DERECHA

# No determinística
def no_deterministica():
    movimiento = random.choice([ARRIBA, ABAJO, IZQUIERDA, DERECHA])
    return movimiento