# Autor: Juan Antonio Cuello
# Ejercicio10_0 - bucle for 

#Recorrer los elementos de una lista
colores = ["rojo","verde","azul"]
for x in colores:
    print(x)

#Recorrer los caracteres de una cadena
nombre="Alicia"
for x in nombre:
    print(x)

#Error al iterar un entero. ¿Como se soluciona?
numero=1234
for x in numero:
    print(x)

#Hacer un for con un determinado numero de pasos
for x in range(6):
    print(x)

#Contar de 1 a 14 de 2 en 2
#parametros del range: (inicio, fin no incluido, salto) 
for x in range(1,15,2): 
    print(x)

#Recorrer los caracreres de una cadena usando len   
nombre="Perico"
for i in range(len(nombre)):
    print(nombre[i])
    
#Hacer la tabla de multiplicar del 5
for x in range(1,11):
    print("5 x ",x,"=",(5*x))


#Imprimir los numeros de la lista hasta encontrar un -1 (usando break)
lista=[2,6,4,-1,4,6]
for x in lista:
    if x==-1:
        break
    print(x)


#Imprimir solo los numeros pares (usando continue)
lista=[2,3,4,-1,5,6]
for x in lista:
    if (x%2!=0):
        continue
    print(x)








#Imprimir las letras no vocales de una palabra
    
