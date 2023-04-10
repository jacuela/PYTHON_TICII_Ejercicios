#Autor: Juan Antonio Cuello
#Ejercicio 10.5 - capitalizar

frase="me encanta programar en python"
palabras=0

print(frase[0].upper(),end="")

for i in range(1,len(frase)):
    
    if (frase[i]==" "):
        palabras+=1
    
    if (frase[i-1]==" "):
        print(frase[i].upper(),end="")
    else:
        print(frase[i],end="")

print()
print("total palabras:",palabras+1)
