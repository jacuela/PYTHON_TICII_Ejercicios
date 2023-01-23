# Autor: Juan Antonio Cuello
# Ejercicio3 - operadores

x=2           
y=3

suma=x+y
multi=x*y
resta=x-y
divi=x/y
print(suma,multi,resta,divi)


print("Redondeo la division a tres decimales:")
divi=round(divi,3)
print(divi)

print("Operador de suma y asignacion. y=y+1")
print("y vale:",y);  
y+=1
print("y+=1 vale:",y)

print("Exponenciación:")
expo=x**y
print(x,"elevado a",y,"es:",expo)

print("Modulo 7%3 (resto de la división entera):")
modulo=7%3
print(modulo)

print("Division entera 15//4:")
division_entera=15//4
print(division_entera)

## El operador + también se puede aplicar a cadenas
## + concatena cadenas
print("- operador + en candenas -")

abecedario="a"+"b"+"c"+"d"+"e"+"..."
print(abecedario)

nombre="Irene"
apellido="Cano"
print("Nombre:"+nombre)
print("Apellido:"+apellido)

nombreCompleto=nombre+" "+apellido    #el + concatena cadenas
print(nombreCompleto)

#No es neceario crear la variable
print(nombre+" "+apellido)
print(nombre,apellido)      #fijate como te mete un espacio al usar , 


#La siguiente linea me da error porque combina una cadena con un numero
#usando el operador +
#Corrígela de dos formas: usando la coma en el print y usando
#la función str(variable) que convierte a cadena una variable numerica

#print("La suma de x e y es:"+suma) 

print("La suma de x e y es:"+str(suma)) 
print("La suma de x e y es:",suma) 



