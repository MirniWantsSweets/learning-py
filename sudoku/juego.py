from funciones import *

# == Variables globales =============================================
max_row_size = ...
max_col_size = ...
...

# == Funcion principal ==============================================
def main():
    # = Crear y inicializar un tablero ====================
    tablero = crearYInicializarUnTablero()
    print(tablero)
    # = Preguntar posicion y valor para insertar ==========
    fila = int(input("Que fila quieres elegir?\n"))
    columna = int(input("Que columna quieres elegir?\n"))
    valor = int(input("Que valor quieres elegir?\n"))

    # = Comprovar si el valor es valido ===================
    #comprobarFila(tablero, 5)
    if fila < 1 or fila > 9:
        return 1

    #comprobarColumna(tablero, 5)
    if columna < 1 or columna > 9:
        return 1

    #comprovarValor
    if valor < 1 or valor > 9:
        return 1
    
    comprobarCuadrado(tablero, 4, 4, 8)

    # = Si no es valido mostrar mensaje de error ==========
    if valor

# == Condicion para encender la funcion principal ===================
if __name__ == "__main__":
    main()