# Autor: Juan Antonio Cuello
# Ejercicio 7_6

dia=input("Dia de la semana:")
dinero=int(input("Dinero en la cuenta:"))

if (dia=="sabado" or dia=="domingo"):
    if (dinero>1000):
        print("Me voy de compras")
    else:
        print("Me quedo en casa viendo la tele")
else:
    print("Me voy a trabajar")
    