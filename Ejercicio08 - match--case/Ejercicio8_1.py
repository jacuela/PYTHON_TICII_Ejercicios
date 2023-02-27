# Autor: Juan Antonio Cuello
# Ejercicio8_1 - menu


print("CALCULADORA SIMPLE")
print("==================")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
opcion=int(input(" Elige opcion:"))

print()
match opcion:
    case 1:
        num1=int(input("Dime el primer numero:"))
        num2=int(input("Dime el segundo numero:"))
        print(num1,"+",num2,"=",(num1+num2))
    case 2:
        num1=int(input("Dime el primer numero:"))
        num2=int(input("Dime el segundo numero:"))
        print(num1,"-",num2,"=",(num1-num2))
    case 3:
        num1=int(input("Dime el primer numero:"))
        num2=int(input("Dime el segundo numero:"))
        print(num1,"*",num2,"=",(num1*num2))
    case 4:
        num1=int(input("Dime el primer numero:"))
        num2=int(input("Dime el segundo numero:"))
        print(num1,"/",num2,"=",round((num1/num2),2))
    case _:
        print("Opcion inválida")

