# Autor: Juan Antonio Cuello
# Ejercicio 7_5

examen1=int(input("Nota del primer examen:"))
examen2=int(input("Nota del segundo examen:"))
examen3=int(input("Nota del tercer examen:"))

entregado=input("Has entregado el trabajo? [S | N]:")

if (entregado == "N"):
    notaEvaluacion=4
else:
    notaEvaluacion=0.3*examen1+0.3*examen2+0.4*examen3

print("La nota de la evaluacion es",round(notaEvaluacion,2))


#Muestro la calificación en formato texto
if (notaEvaluacion<5):
    print("Ohhhhhhh, estas suspenso")
elif (notaEvaluacion>=5 and notaEvaluacion<6):
    print("SUFICIENTE")
elif (notaEvaluacion>=5 and notaEvaluacion<7):
    print("BIEN")
elif (notaEvaluacion>=7 and notaEvaluacion<9):
    print("NOTABLE")
elif (notaEvaluacion>=9):
    print("SOBRESALIENTE")
