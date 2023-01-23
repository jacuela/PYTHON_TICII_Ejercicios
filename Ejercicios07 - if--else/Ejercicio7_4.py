# Autor: Juan Antonio Cuello
# Ejercicio 6_4

nombre1=input("Dime el nombre1:")
nombre2=input("Dime el nombre2 (INTRO si no tienes):")
apellido1=input("Dime el apellido1:")
apellido2=input("Dime el apellido2:")


if (nombre2!=""):
    print("Tus iniciales son -->   ",nombre1[0],nombre2[0],apellido1[0],apellido2[0])
    
else:
    print("Tus iniciales son -->   ",nombre1[0],apellido1[0],apellido2[0])
    