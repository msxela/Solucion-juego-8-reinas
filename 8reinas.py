global reina
global numero
OCHO = 8 # Definir la capacidad máxima de la pila
reina = [None] * 8 #Almacenar la posición de fila de 8 reinas
 
numero = 0 # Calcula el número total de soluciones
 #Decide dónde guardar la reina
 #Output el resultado requerido
def print_table():
    global numero
    x=y=0
    numero+=1
    print('')
    print ('La %d solución al problema de las ocho reinas \ t'% numero)
    for x in range(OCHO):
        for y in range(OCHO):
            if x==reina[y]:
                print('<R>',end='')
            else:
                print('<->',end='')
        print('\t')
        input ('\ n .. presione cualquier tecla para continuar .. \ n')
 
 #Prueba si la reina en (fila, col) está siendo atacada
 # Si es atacado, el valor devuelto es 1, de lo contrario devuelve 0
def attack(row,col):
    global reina
    i=0
    atk=0
    offset_row=offset_col=0
    while (atk!=1)and i<col:
        offset_col=abs(i-col)
        offset_row=abs(reina[i]-row)
                 # Juzga si las dos reinas están en la misma línea o en la misma diagonal
        if reina[i]==row or offset_row==offset_col:
            atk=1
        i=i+1
    return atk
 
def decide_position(value):
    global reina
    i=0
    while i<OCHO:
        if attack(i,value)!=1:
            reina[value]=i
            if value==7:
                print_table()
            else:
                decide_position(value+1)
        i=i+1
 
 #Programa principal
decide_position(0)