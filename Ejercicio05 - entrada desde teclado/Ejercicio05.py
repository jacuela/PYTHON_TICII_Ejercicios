# Autor: Juan Antonio Cuello
# Ejercicio05 - entrada desde teclado

#Pedir por teclado el nombre y la edad
nombre=input("nombre:")
edad=int(input("edad:"))    #falta convertirlo a entero

print("Te llamas",nombre,"y tienes",edad,"años.")

print("Tu edad multiplicada por 10 es:")
edad=edad*10
print(edad)

#Pedir tu estatura y tu peso y calcular el IMC
print();
print("-- Calculo del IMC --")
altura=float(input("altura en metros:"))
peso=int(input("peso:"))

_IMC=peso/(altura*altura)


print(nombre,"tu IMC es",round(_IMC,2))

#Buscar como mostrar el IMC con dos decimales

