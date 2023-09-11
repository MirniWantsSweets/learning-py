class Tablero:
    def __init__(self):
        "Funcion que sirve para crear y inicializar un tablero y devolverlo."
        fila = []
        for x in range(9):
            fila.append(-1)

        tablero = []
        for x in range(9):
            tablero.append(fila[:])
        self.tablero = tablero
    
    # == Funciones para comprobar la validez del movimiento del jugador =========================

    def compruebaFila(self, fila: int, valor: int) -> bool:
        "Funcion que comprueba si la fila especificada es valida."
        for x in range(0,9):
            if self.tablero[fila][x] == valor:
                return False
        return True

    def compruebaColumna(self, columna: int, valor: int) -> bool:
        "Funcion que comprueba si la columna especificada es valida."
        for x in range(0,9):
            if self.tablero[x][columna] == valor:
                return False
        return True    

    def compruebaCuadrado(self, fila: int, columna: int, valor: int) -> bool:
        "Funcion que comprueba si el cuadrado especificado es valido."
        sumarAFila = (int(fila/3))*3
        sumarAColumna = (int(columna/3))*3

        for x in range(0,3):
            for y in range(0,3):
                if self.tablero[x + sumarAFila][y + sumarAColumna] == valor:
                    return False
        return True
    
    # == Funciones complementarias ==============================================================

    def cambiarValor(self, fila, columna, valor) -> None:
        "Funcion que sirve para actualizar el valor de x fila y x columna"
        #Falta acabar la linea de abajo
        self.tablero

    def __str__(self) -> None:
        "Metodo que imprime un tablero de manera bonita para jugar"
        res = "--------------------------------------------------\n"
        res += "--------------------------------------------------\n"
        need_double_line = 1
        for linea in self.tablero:
            res = res + "|| " + str(linea[0]) + " | " + str(linea[1]) + " | " + str(linea[2]) + " || " + str(linea[3]) + " | " + str(linea[4]) + " | " + str(linea[5]) + " || " + str(linea[6]) + " | " + str(linea[7]) + " | " + str(linea[8]) + " ||\n"
            res = res + "--------------------------------------------------\n"
            if need_double_line == 3:
                res = res + "--------------------------------------------------\n"
                need_double_line = 1
            else:
                need_double_line += 1
        return res