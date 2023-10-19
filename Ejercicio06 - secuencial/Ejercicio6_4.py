# Autor: Juan Antonio Cuello
# Ejercicio 6_4

print("=== INVERTIR ===")
numInt=int(input("Dime un número (de dos cifras):"))

numCadena=str(numInt);

unidades=numCadena[1];
decenas=numCadena[0];
print("El número invertido es: "+unidades+decenas)




''' otra forma de hacerlo
unidades=num%10
decenas=num//10

print("El número invertido es:"+str(unidades)+str(decenas))
'''