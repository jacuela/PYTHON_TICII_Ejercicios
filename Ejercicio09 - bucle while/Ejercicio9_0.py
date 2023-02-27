# Autor: Juan Antonio Cuello
# Ejercicio9_0 - bucle while

#Repetir una frase
repeticiones=1
while repeticiones<=10:
    print("No volveré a decir palabrotas")
    repeticiones=repeticiones+1

#Tabla de multiplicar
numero=int(input("Dime un numero:"))
i=1

print("============================")
print("Tabla de multiplicar del",numero)
while i<=10:
    print(numero,"x",i,"=",(numero*i))
    i+=1;
else:
    print("=========================")

#Introducir por teclado numeros y decir si son par o impar. Parar con un 0
numero=int(input("Dime un numero [0 para terminar]:"))
while numero!=0:
    if (numero%2==0):
        print(numero,"  PAR")
    else:
        print(numero,"  IMPAR")
    numero=int(input("Dime un numero:"))
else:
    print("fin del bucle. bye bye")
   
   
   
#Introducir por teclado numeros y decir si son par o impar. Parar con un 0
#usando break y bucle infinito  

while True:
    numero=int(input("Dime un numero [0 para terminar]:"))
    if (numero==0):
        break
    elif (numero%2==0):
        print(numero,"  PAR")
    else:
        print(numero,"  IMPAR")
   


#Introducir contraseña (infinitas posibilidades)
print("EJERCICIO - CONTRASEÑA")    
password="abracadabra"
passwordUsuario=input("Dime la contraseña:")
while passwordUsuario!=password:
    print("contraseña incorrecta")
    passwordUsuario=input("Dime la contraseña:")
else:
    print("Has entrado!!")


#Acumuladores y contadores
print("EJERCICIO - ACUMULADORES Y CONTADORES")    
numero=int(input("Dime un numero [0 para terminar]:"))
contador=0    #inicializo el contador
suma=0  #inicializo el acumulador 
while numero!=0:
    contador+=1
    suma=suma+numero
    
    #Leo el siguiente numero a analizar
    numero=int(input("Dime un numero:"))
else:
    print("He introducido",contador,"numeros")
    print("La suma de todos ellos es",suma)





