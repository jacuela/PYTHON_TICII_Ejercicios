#Autor: Juan Antonio Cuello
#Ejercicio 11.3 - bola mágica
import random


respuestas = ["SI","NO","PUEDE","NI EN SUEÑOS!!","SEGURO!!"]

pregunta = input("Hazme una pregunta [INTRO para fin]:")
while (pregunta != ""):
    aleatorio = random.randint(0,4)
    print(respuestas[aleatorio])
    print("----------------------------")
    pregunta = input("Hazme una pregunta  [INTRO para fin]:")


