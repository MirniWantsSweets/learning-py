from funciones import *

# == Variables globales =============================================
max_row_size = ...
max_col_size = ...
...

# == Funcion principal ==============================================
def main():
    # = Crear y inicializar un tablero ====================
    tablero = Tablero()
    print(tablero)
    # = Preguntar posicion y valor para insertar ==========
    
    # == Preguntamos la fila hasta obtener un valor de fila valido
    while fila < 1 or fila > 9:
        fila = int(input("Que fila quieres elegir?\n"))
    
    # == Preguntamos la columna hasta obtener un valor de columna valido
    while columna < 1 or columna > 9:
        columna = int(input("Que columna quieres elegir?\n"))
    
    # == Preguntamos el valor hasta obtener un valor valido
    while valor < 1 or valor > 9:
        valor = int(input("Que valor quieres elegir?\n"))

    # = Llegados a este punto tenemos un tablero creado y inicializado
    # = y las variables fila, columna y valor

    # = Comprobamos que los valores introducidos se puedan meter en la tabla
    # == Comprobamos si se pueden meter en la fila

    # == Comprobamos si se pueden meter en la columna

    # == Comprobamos si se pueden meter en el cuadrado
    
    # Tienes que utilizar las siguientes funciones:
    #tablero.compruebaFila()
    #tablero.compruebaColumna()
    #tablero.compruebaCuadrado()

    # = Si no es valido mostrar mensaje de error ==========

    # = Si es valido cambiar el valor de la posicion por el valor obtenido

# == Condicion para encender la funcion principal ===================
if __name__ == "__main__":
    main()


#####################################################################
# Codigo viejo
#####################################################################

# # = Comprobar si el valor es valido ===================
# #tablero.compruebaFila(tablero, 5)
# if fila < 1 or fila > 9:
#     return 1

# #tablero.compruebaColumna(tablero, 5)
# if columna < 1 or columna > 9:
#     return 1

# #comprovarValor
# if valor < 1 or valor > 9:
#     return 1