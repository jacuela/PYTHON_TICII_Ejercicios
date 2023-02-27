# Autor: Juan Antonio Cuello
# Ejercicio9_2 - mayor y media


print("EJERCICIO 9_2 - MAYOR Y MEDIA")
numero=int(input("Dime un numero [0 para terminar]:"))

mayor=numero      #inicializo mayor al primer numero (para permitir positivos y negativos)
suma=0       #inicializo media a 0
contador=0   #inicializo contador de numeros introducidos

while numero!=0:
    if numero>mayor:
        mayor=numero
        
    contador+=1
    suma=suma+numero
    
    #Leo el siguiente numero a analizar
    numero=int(input("Dime un numero [0 para terminar]:"))
else:
    print("El mayor es el",mayor)
    print("La media es",round((suma/contador),2))
    
    
