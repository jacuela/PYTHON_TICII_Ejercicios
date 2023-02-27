# Autor: Juan Antonio Cuello
# Ejercicio9_4ejemplo - circulos de colores 

print("EJERCICIO 9_4ejemplo - circulos de colores ")

#------inicialización
from turtle import *
setup(250, 250, 0, 0)
screensize(200, 200)
colormode(255)
#-------------------

penup()  #para evitar pintar linea al mover cursor
goto(-50,50)
dot(50, "green")

goto(50,-50)
dot(100, 240,0,240)

done() #fin de la tortuga


