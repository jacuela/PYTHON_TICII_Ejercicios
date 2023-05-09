#Autor: Juan Antonio Cuello
#Ejercicio 11.0 - listas

'''
#Me creo una lista, muestro el tamaño e imprimo la lista. Accece a algunos
#elementos con la notación "lista[indice]"
lista1 = ["perro","gato","ratón"]
print("Elementos de la lista:",len(lista1))
print("La lista completa:",lista1)
print("primer elemento:",lista1[0])
print("último elemento:",lista1[len(lista1)-1])
print("elemento en la posición 1:",lista1[1])

#Puedo añadir elementos a la lista al final, cambiar elementos y borrar elementos
lista1.append("jirafa")
lista1[0]="nuevo perro"
lista1.remove("ratón")
print(lista1)


#Puedo recorrer de uno en uno los elementos de una lista (sin usar índices) y hacer el
#tratamiento que quiera a cada elemento
lista2 = [2,4,1,5,7]
for x in lista2:
    print(x)
    if (x%2==0):
        print("-->",x,"es par")

print("-------------------------------------------")

#El recorrido se puede hacer usando índices. Mismo ejercicio pero indicando impares
for i in range(len(lista2)):
    print(lista2[i])
    if (lista2[i]%2!=0):
        print("-->",lista2[i],"es impar")        

print("-------------------------------------------")
'''
'''
#Puedo comprobar si un elemento esta en una lista de dos maneras
lista3 = [2,6,9,10,4]
print(lista3)
numero = int(input("Dime un número: "))   #el nunero a buscar en la lista

#OPCION 1 - recorriendo la lista y comparando. Así se hace en muchos lenguajes
encontrado = False
for x in lista3:
    if x==numero:
        encontrado = True

if encontrado==True:
    print("Sí, el numero",numero,"sí está en la lista")
else:
    print("Nooop, el numero",numero,"no está en la lista")


#OPCION 2 - python tiene un atajo, la instrucción "if VALOR in LISTA"
if numero in lista3:
    print("Sí, el numero",numero,"sí está en la lista")
else:
    print("Nooop, el numero",numero,"no está en la lista")
'''


''' 
#Puedo usar un bucle for para rellenar una lista con valores pedidos
#por teclado
milista = []  #lista vacia
tam = int(input("Total elementos de la lista: "))
for i in range(tam):
    elemento = input("Nombre del pais "+str(i+1)+": ")
    milista.append(elemento)
print(milista)
'''

#Matriz: lista de listas / listas anidadas
lista = [[1,2,3],[4,5,6],[7,8,9]] #matriz de 3x3
#   lista[0] --> [1, 2, 3]
#   lista[1] --> [4, 5, 6]
#   lista[2] --> [7, 8, 9]

#Recorrer la matriz por filas
for i in range(len(lista)):
    print("fila",i)
    for j in range(len(lista[0])):
        print(lista[i][j])







