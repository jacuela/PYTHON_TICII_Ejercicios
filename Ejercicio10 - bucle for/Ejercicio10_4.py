#Autor: Juan Antonio Cuello
#Ejercicio 10.4 - contar palabras

frase=input("Dine una frase: ")
palabras=0

for i in range(len(frase)):
    if (frase[i]==" "):
        palabras+=1
   
print()
print("total palabras:",palabras+1)
