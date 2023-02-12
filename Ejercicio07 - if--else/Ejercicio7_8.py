# Autor: Juan Antonio Cuello
# Ejercicio 7_8
   
año=int(input("Dime un año:"))

if (año%4==0 and año%100!=0):
    print("El año",año,"Sí es bisiesto")
    
elif(año%100==0 and año%400==0):
        print("El año",año,"Sí es bisiesto")
else:
        print("El año",año,"NO es bisiesto")


#Otra forma de hacerlo es con una condición cúadruple
        
if ((año%4==0 and año%100!=0) or (año%100==0 and año%400==0)):
    print("El año",año,"Sí es bisiesto")
else:
    print("El año",año,"NO es bisiesto")
    