# Autor: Juan Antonio Cuello
# Ejercicio 7_3

mes=int(input("Dime el mes:"))

if mes==1:
    print("31 días")
elif mes==2:
    print("28 días")
elif mes==3:
    print("31 días")
elif mes==4:
    print("30 días")
elif mes==5:
    print("31 días")
elif mes==6:
    print("30 días")
elif mes==7:
    print("31 días")
elif mes==8:
    print("31 días")
elif mes==9:
    print("30 días")
elif mes==10:
    print("31 días")
elif mes==11:
    print("30 días")
elif mes==12:
    print("31 días")    
else:
    print("Mes incorrecto")


#Usando condiciones multiples
if mes==1 or mes==3 or mes==5 or mes==8 or mes==7 or mes==10 or mes==12:
    print("31 días")
elif mes==2:
    print("28 días")
elif mes==4 or mes==5 or mes==9 or mes==11:
    print("30 días")
else:
    print("Mes incorrecto")
    

