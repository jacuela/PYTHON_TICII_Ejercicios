# Autor: Juan Antonio Cuello
'''
    Ejercicio04.py
    Este programa dibuja un cuadrado usando la librería turtle
'''


from turtle import *

setup(600, 600, 0, 0) #tamaño de la ventana 600x600 (anchoxalto)
screensize(500,500)  #tamaño del lienzo para escribir
colormode(255)
title("Figuras")
hideturtle()



dot(10,255,0,0)  #dibujo un punto en la posicion inicial 0,0
penup()          #levanto el lapiz

#Dibujo cuadrado
goto(-50, -50)   #me desplazo al punto inicial
pendown()
goto(50,-50)   #linea de abajo
goto(50,50)    #linea de derecha
goto(-50,50)   #linea arriba
goto(-50,-50)  #linea 
penup()

#Dibujo tejado
goto(50,50)
pendown()
goto(0,100)
goto(-50,50)
penup()

#Dibujo suelo
goto(-200,-50)
pendown()
goto(200,-50)
penup()

#Dibujo arbol
goto(150,-50)
pendown()

goto(150,20)
pensize(5)
circle(50)









