#Autor: Juan Antonio Cuello
#Ejercicio 10.3 - nombre con gjuiones

 
nombre=input("Dime tu nombre: ")
'''
#Trato especial del ultimo caracter
for i in range(len(nombre)):
    
    if (i==len(nombre)-1):
        print(nombre[i],end="")
        
    else:
        print(nombre[i]+"-",end="")
        
'''

#Trato especial del primer caracter
for i in range(len(nombre)):
    
    if (i==0): #estoy en el primer caracater
        print(nombre[i],end="")
        
    else:
        print("-"+nombre[i],end="")




#Otra forma de hacer el else
'''
else:
    print(nombre[i],end="")
    print("-",end="")
'''    

    
    