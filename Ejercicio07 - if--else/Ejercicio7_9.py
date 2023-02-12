# Autor: Juan Antonio Cuello
# Ejercicio 7_9

dia=int(input("Dime el dia:"))
mes=int(input("Dime el mes:"))
año=int(input("Dime el año:"))

#diaCorrecto=false
#mesCorrecto=false
#añoCorrecto=fasle

#Comprobamos el año
if (año>1900 and año<2500):
    añoCorrecto=True
else:
    añoCorrecto=False

#Comprobamos el mes
if (mes>=1 and mes<=12):
    mesCorrecto=True
else:
    mesCorrecto=False

#Comprobamos el dia
if (mes==1 or mes==3 or mes==5 or
    mes==7 or mes==8 or mes==10 or mes==12):
    if (dia>=1 and dia<=31):
        diaCorrecto=True
    else:
        diaCorrecto=False
elif (mes==4 or mes==6 or mes==9 or mes==11):
    if (dia>=1 and dia<=30):
        diaCorrecto=True
    else:
        diaCorrecto=False
elif (mes==2):
    #Si el año es bisiesto, son 29 dias
    if ((año%4==0 and año%100!=0) or (año%100==0 and año%400==0)):
        if (dia>=1 and dia<=29):
            diaCorrecto=True
        else:
            diaCorrecto=False
    else:
        if (dia>=1 and dia<=28):
            diaCorrecto=True
        else:
            diaCorrecto=False
else:
    diaCorrecto=False


#Analizamos los booleanos
if (diaCorrecto==True and mesCorrecto==True and
    añoCorrecto==True):
    print("La fecha",dia,"/",mes,"/",año,"es CORRECTA")
else:
    print("La fecha",dia,"/",mes,"/",año,"es INCORRECTA")
    
    
    
    

