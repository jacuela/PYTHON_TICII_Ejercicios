# Autor: Juan Antonio Cuello
# Ejercicio02 - variables



print("- imprimo valores-")
x=69           #x es de tipo entero
y="Juanito"    #y es de tipo cadena (String)
print(x)
print(y)

print("- el tipo de una variable puede cambiar -")
z="Celia";    #en este punto, z de de tipo cadena
print(z)
z=10;       #en este punto, z es de tipo entero
print(z)

print("- el nombre de variables es case sensitive -")
a="Pedro";
A='Alicia';    #puedo usar comillas simples
print(a)   
print(A)

#print puede imprimir varios valores
print(y,"esta colado por",A)

#el nombre de variables puede ser diverso
#no puede tener espacios y debe empezar por minusculas preferiblemente
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"  #en mayusculas mejor NO

#ojo al intercambiar dos variables
print("- intercambio con pérdida -")
x=15
y=30
y=x
x=y
print(x)
print(y)

print("- intercambio usando variable auxiliar -")
unNumero=15          
otro_numero=30

z=unNumero
unNumero=otro_numero
otro_numero=z
print(unNumero)
print(otro_numero)

