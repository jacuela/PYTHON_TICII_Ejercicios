# Autor: Juan Antonio Cuello
# Ejercicio9_1 - contador positivos y negativos


print("EJERCICIO 9_1 - CONTADOR POSITIVOS Y NEGATIVOS")
numero=int(input("Dime un numero [0 para terminar]:"))

totalPositivos=0
totalNegativos=0

while numero!=0:
    if numero>0:
        totalPositivos+=1
    if numero<0:
        totalNegativos+=1
    
    #Leo el siguiente numero a analizar
    numero=int(input("Dime un numero [0 para terminar]:"))
else:
    print("Positivos introducidos:",totalPositivos)
    print("Negativos introducidos:",totalNegativos)

    
