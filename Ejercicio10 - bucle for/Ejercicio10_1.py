#Autor: Juan Antonio Cuello
#Ejercicio 10.1 - factorial y suma

N=int(input("Dime un numero entero positivo: "))

while N<0:
    print("  >ERROR: solo enteros")
    N=int(input("Dime un numero entero positivo: "))

factorial=1
suma=0
for x in range(1,N+1):
    suma=suma+x
    factorial=factorial*x
    
print("La suma de los",N,"primeros numeros es: ",suma)
print("El factorial de ",N,"es: ",factorial)


    
    