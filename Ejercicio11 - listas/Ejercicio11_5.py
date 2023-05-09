#Autor: Juan Antonio Cuello
#Ejercicio 11_5 - sumas de filas y columnas


matriz = [[1,1,8],[2,2,5],[3,8,7],[4,7,4],[5,9,6]]

totalFilas = 5
totalColumnas = 3
totalFila = 0

#Recorremos la tabla por filas
for fila in range(totalFilas):
    totalFila = 0   #reseteo la suma de la fila
    for columna in range(totalColumnas):
        print(matriz[fila][columna]," ",end="")
        totalFila = totalFila + matriz[fila][columna]
    print("Total fila:",totalFila)
    print()











'''
suma_fila = 0
suma_columna = 0

#Recorro por filas para sumar las filas
for i in range(5):
    suma_fila = 0
    for j in range(3):
        print("\033[30;43m",matriz[i][j],"   ",end="")
        suma_fila = suma_fila + matriz[i][j]
    print("\033[31;44m",suma_fila,"\033[0;m")


#Recorro por columnas para sumar las columnas. Esta vez no muestro nada
for j in range(3): #3 columnas
    suma_columna = 0
    for i in range(5): #5 filas
        #print("\033[30;43m",matriz[i][j],"   ",end="")
        suma_columna = suma_columna + matriz[i][j]
    print("\033[31;42m",suma_columna,"  ",end="")
    #print()

'''
        