#Autor: Juan Antonio Cuello
#Ejercicio 11.4 - bonoloto
import random

mis_numeros = []
lista_premiados = []
total_introducidos = 0

while total_introducidos < 6:
    num = int(input("Dime el numero "+str(total_introducidos+1)+": "))
    if (num>=1 and num<=49):
        mis_numeros.append(num)
        total_introducidos+=1
    else:
        print("Numero incorrecto. Debe estar entre 1 y 49")

print("Mis numeros:",mis_numeros)

print("------ jugando ------")
total_aciertos = 0
for x in range(6):
    aleatorio=random.randint(1,49)
    lista_premiados.append(aleatorio)
    if aleatorio in mis_numeros:
        total_aciertos+=1

print("Lista de premiados:",lista_premiados)
print("Total aciertos:\033[30;41m",total_aciertos,"\033[0;m")

