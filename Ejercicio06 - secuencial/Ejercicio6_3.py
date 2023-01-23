# Autor: Juan Antonio Cuello
# Ejercicio 6_3

print("=== CALIFICACION  ===")
parcial1=int(input("Nota del primer parcial: "))
parcial2=int(input("Nota del segundo: "))
parcial3=int(input("Nota del tercer : "))
final=int(input("Nota del examen final: "))

media_parciales=(parcial1+parcial2+parcial3)/3

nota_evaluacion=media_parciales*0.6+final*0.4
print("Tienes un --> ",round(nota_evaluacion,2))

