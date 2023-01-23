# Autor: Juan Antonio Cuello
# Ejercicio3

#Tipo cadena (str)
cadena='hola'
print(cadena)

#Tipo entero (int)
num_entero=69
print(num_entero)

#Tipo decimal (float)
num_decimal=3.14
print(num_decimal)

#Tipo booleano (bool)
mayor_de_edad=True
es_rojo=False
print(mayor_de_edad)

(3==4)  #una comparación devuelve True o False
print((3==4))


#Tipo lista (indexada, permite repetir)
lista1=["Pedro","Maria","Alicia"]
print("lista1:",lista1)

lista_vacia=[]
print("lista vacia:",lista_vacia)

lista2=[5,66,-20,25,30]
print("lista2:",lista2)
print("Primer elemento:",lista2[0])
print("Tercer elemento:",lista2[2])


#Tipo conjunto (no indexada, no se permiten repeticiones)
conjunto={"naranja","limon","pera","limon","pera"}
print("Todo el conjunto:",conjunto)
#print("Primer elemento:",conjunto[0])  #error. No indexable




#********************************
#Conversion entre tipos (casting)
#*******************************

#convertir de entero a cadena
x=str(76)
print(x,"es de tipo",type(x))

#convertir de cadena a entero --> no siempre
x=int("69")
print(x,"es de tipo",type(x))

#error de conversion
#x=int('hola')   
#print(x,"es de tipo",type(x))

#convertir de decimal a entero y viceversa
x=int(3.13)
print(x,"es de tipo",type(x))

x=float(5)
print(x,"es de tipo",type(x))








