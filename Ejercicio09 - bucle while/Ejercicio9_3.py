# Autor: Juan Antonio Cuello
# Ejercicio9_3 - adivina numero
import random

print("EJERCICIO 9_3 - ADIVINA NUMERO")

print("ADIVINA UN NUMERO ENTRE 0 y 9")
acertado=False
aleatorio=random.randint(0,9)

numero=int(input("Adivina el numero??? :"))
while (numero!=aleatorio):
    if (numero>aleatorio):
        print("-menor-")
        numero=int(input("Adivina el numero??? :"))
    elif(numero<aleatorio):
        print("-mayor-")
        numero=int(input("Adivina el numero??? :"))
        
else:
    print("Has acertado!")