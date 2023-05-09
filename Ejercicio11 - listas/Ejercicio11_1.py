#Autor: Juan Antonio Cuello
#Ejercicio 11_1
'''
#Ejercicio normal
lista1 = [1,3,5,7,9]
lista2 = [9,7,5,3,1]

lista_suma = []
for i in range(len(lista1)):
    lista_suma.append(lista1[i]+lista2[i])

print(lista1)
print(lista2)
print(lista_suma)
'''

#Mejora
import random

lista1 = []
lista2 = []
for i in range(5):
    lista1.append(random.randint(1,10))
    lista2.append(random.randint(1,10))
lista_suma = []
for i in range(len(lista1)):
    lista_suma.append(lista1[i]+lista2[i])

print(lista1)
print(lista2)
print(lista_suma)
    
    
