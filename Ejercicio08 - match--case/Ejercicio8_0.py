# Autor: Juan Antonio Cuello
# Ejercicio08 - match..case

dia=int(input("Dime un dia de la semana [1-7]:"))

match dia:
    case 1:
        print("Lunes")
        print("El peor dia")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
        print("Me voy de fiesta")
    case 6:
        print("Sabado")
        print("El mejor día")
    case 7:
        print("Domingo")
        print("Hoy como arroz y pavo. Agggghh!!!!")
    case _:
        print("Dia incorrecto")

        

