numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

while True:

    print("Las opciones disponibles son: \n Opcion 1: sumar \n Opcion 2: restar \n Opcion 3: multiplicar \n Opcion 4: salir")

    opcion = int(input("Ingrese número de opcion: "))
    if opcion == 1:
        print(f"La suma de {numero1} + {numero2} es:", numero1 + numero2)
    elif opcion == 2:
        print(f"La resta de {numero1} - {numero2} es:", numero1 - numero2)
    elif opcion == 3:
        print(f"El producto entre {numero1} y {numero2} es:", numero1 * numero2)
    elif opcion == 4:
        print("Salir del programa")
        break
    else:
        print("La opcion indicada no es correcta")
