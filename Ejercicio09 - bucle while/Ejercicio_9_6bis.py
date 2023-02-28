#Decir si un numero es de la buena o mala suerte

numero=input("dime un numero: ")

i=0
contadorBuena=0
contadorMala=0
while i<len(numero):
    print(numero[i])
    if (numero[i]=="2" or numero[i]=="5" or numero[i]=="8"):
        contadorBuena+=1
    else:
        contadorMala+=1
    i+=1
else:
    if (contadorBuena>=contadorMala):
        print("El numero",numero," es la de BUENA SUERTE")
    else:
        print("El numero",numero," es la de MALA SUERTE")
    
    