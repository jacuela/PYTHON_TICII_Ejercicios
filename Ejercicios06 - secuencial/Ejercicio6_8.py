# Autor: Juan Antonio Cuello
# Ejercicio 6_8

print("=== CALCULO DE DINERO ===")
mon2e=int(input("Monedas de 2€:"))
mon1e=int(input("Monedas de 1€:"))
mon50c=int(input("Monedas de 50cent:"))
mon20c=int(input("Monedas de 20cent:"))
mon10c=int(input("Monedas de 10cent:"))


#OPCION1 - calculo todo en euros
print()
todoEuros=mon2e*2+mon1e*1+mon50c*0.5+mon20c*0.2+mon10c*0.1
print("OPCION1")
print ("  Todo en EUROS es:",todoEuros,"€")
euros=int(todoEuros)
centimos= (todoEuros*100)%100
print ("  Equivale a",euros,"€ y",int(centimos),"centimos")

#OPCION2 - saco los euros y los centimos
print()
euros=mon2e*2+mon1e*1
centimos=mon50c*50+mon20c*20+mon10c*10
print("OPCION2")
print ("  Tengo",euros,"€ y",centimos,"centimos")

eurosExtra=int(centimos/100)
centimosQueQuedan=centimos%100

euros=euros+eurosExtra;
centimos=centimosQueQuedan
print ("  Equivale a",euros,"€ y",int(centimos),"centimos")




