# Autor: Juan Antonio Cuello
# Ejercicio9_4 - pintura abstracta 

print("EJERCICIO 9_4 - pintura abstracta ")

import random
from turtle import *

setup(250, 250, 0, 0)
screensize(200, 200)
colormode(255)


aleatorio=random.randint(0,9)
totalCirculos=100

i=0
while i<totalCirculos:
    penup()
    
    #generamos valores aleatorios
    #para generar la componente x e y,
    #pongo 150 (no 200) para no pintar muy en el borde
    x=random.randint(-150,150) 
    y=random.randint(-150,150)
    radio=random.randint(10,60)
    R=random.randint(0,255)
    G=random.randint(0,255)
    B=random.randint(0,255)
    
    print(x,y)
    goto(x,y)
    #pendown()
    dot(radio, R,G,B)
    
    i+=1
done()


