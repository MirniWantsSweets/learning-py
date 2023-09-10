# == Funciones complementarias del programa =========================

def comprobarFila(tablero, fila, valor):
    "Funcion que comprueba si la fila especificada es valida."
    for x in range(0,9):
        if tablero[fila][x] == valor:
            return False
    return True

def comprobarColumna(tablero, columna, valor):
    "Funcion que comprueba si la columna especificada es valida."
    for x in range(0,9):
        if tablero[x][columna] == valor:
            return False
    return True    

def comprobarCuadrado(tablero, fila, columna, valor):
    "Funcion que comprueba si el cuadrado especificado es valido."
    sumarAFila = (int(fila/3))*3
    sumarAColumna = (int(columna/3))*3

    for x in range(0,3):
        for y in range(0,3):
            if tablero[x + sumarAFila][y + sumarAColumna] == valor:
                return False
    return True 

def crearYInicializarUnTablero() -> list:
    "Funcion que sirve para crear y inicializar un tablero y devolverlo."
    fila = []
    for x in range(9):
        fila.append(-1)

    tablero = []
    for x in range(9):
        tablero.append(fila[:])

    return tablero   
