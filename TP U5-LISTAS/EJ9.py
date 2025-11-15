#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
#• Inicializarlo con guiones "-" representando casillas vacías. 
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
#• Mostrar el tablero después de cada jugada.


tateti =[["-" , "-" , "-"] ,
         ["-" , "-" , "-"] ,
         ["-" , "-" , "-" ]]

def tablero():
    print(" TA-TE-TI!!!")
    for i in tateti:
        print(i)

def casilla_vacia(fila, columna):
    # verifico si la casilla está vacía
    if tateti[fila][columna] in ("X", "O"):
        print(" Esa casilla ya está ocupada ")
        return False
    return True

def marcar_cruz():

    tateti[fila][columna]="X"
    print(" MOVIEMIENTO REALIZADO !!! ")
    return True

def marcar_circulo():
    tateti[fila][columna]="O"
    print(" MOVIEMIENTO REALIZADO !!! ")
    return True

while True:

    tablero()
   
   # tunrbo de jugador EQUIS "X"
    fila= input("INDIQUE NUMERO DE FILA DEL 1 AL 3 PARA COLOCAR UNA 'X' ").strip()
    #valido entrada
    if fila.isdigit():
        fila = int(fila)
        if 0<fila<4:
                fila =fila - 1
    else:
        print("CORDENADAS INVALIDAS")
        pass
    
    columna= input("INDIQUE NUMERO DE COLUMNA DEL 1 AL 3 PARA COLOCAR UNA 'X'").strip()
        #valido entrada
    if columna.isdigit():
        columna = int(columna)
        if 0<columna<4:
                columna = columna - 1
    else:
            print("CORDENADAS INVALIDAS")
    
   
    if casilla_vacia(fila,columna):
            # si se marcó bien, pasa el turno
            pass
    else:
        # si falla, vuelve a pedir
            continue

    marcar_cruz()

    # tunrbo de jugador CIRCULO "O"
    fila= input("INDIQUE NUMERO DE FILA DEL 1 AL 3 PARA COLOCAR UNA 'O' ").strip()
    #valido entrada
    if fila.isdigit():
        fila = int(fila)
        if 0<fila<4:
                fila =fila - 1
    else:
        print("CORDENADAS INVALIDAS")
        pass
    
        columna= input("INDIQUE NUMERO DE COLUMNA DEL 1 AL 3 PARA COLOCAR UNA 'O'").strip()
        #valido entrada
        if columna.isdigit():
            columna = int(columna)
            if 0<columna<4:
                columna = columna - 1
        else:
            print("CORDENADAS INVALIDAS")

    if casilla_vacia(fila, columna):
        pass
    else:
        continue

    marcar_circulo()