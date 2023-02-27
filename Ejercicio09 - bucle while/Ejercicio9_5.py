# Autor: Juan Antonio Cuello
# Ejercicio9_X - caja fuerte de 3 intentos


print("EJERCICIO 9_X - CAJA FUERTE")

password="abracadabra"
intentos=3

passwordUsuario=input("Dime la contraseña [intentos restantes:"+str(intentos)+"]:")
while passwordUsuario!=password:
    #print("contraseña incorrecta")
    intentos=intentos-1
    if intentos==0:
        break
    passwordUsuario=input("Dime la contraseña [intentos restantes:"+str(intentos)+"]:")
    
if intentos==0:
    print("Caja bloqueada")
else:
    print("Has entrado!!!")

