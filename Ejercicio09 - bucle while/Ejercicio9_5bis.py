# Autor: Juan Antonio Cuello
# Ejercicio9_Xbis - caja fuerte de 3 intentos


print("EJERCICIO 9_Xbis - CAJA FUERTE")

password="x"
intentos=3
acertado=False

passwordUsuario=input("Dime la contraseña [intentos restantes:"+str(intentos)+"]:")
if passwordUsuario==password:
        acertado=True
else:
        intentos=intentos-1
while acertado==False and intentos>0:
    #print("contraseña incorrecta")
    passwordUsuario=input("Dime la contraseña [intentos restantes:"+str(intentos)+"]:")
    if passwordUsuario==password:
        acertado=True
    else:
        intentos=intentos-1
    
if acertado==False:
    print("Caja bloqueada")
else:
    print("Has entrado!!!")

