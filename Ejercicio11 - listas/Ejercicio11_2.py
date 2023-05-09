#Autor: Juan Antonio Cuello
#Ejercicio 11.2 - altura media y edades max y min

alturas=[1.70,1.73,1.68,1.64] 
edades=[16,18,16,19]

sumaAlturas=0
maxEdad = edades[0]
minEdad = edades[0]

#Sumo las alturas
for x in alturas:
    sumaAlturas +=x

#Busco el max y el min. Uso solo un bucle
for x in edades:
    if (x>maxEdad):
        maxEdad=x
    if (x<minEdad):
        minEdad=x

#Muestro resultados
print("Alturas:",alturas)
print("Edades",edades)
print("  -Altura media:",round(sumaAlturas/len(alturas),2))
print("  -Edad máxima:",maxEdad)
print("  -Edad mínima:",minEdad)

