n1 = input("Ingresa el primer numero:")
n2 = input("Ingresa el segundo numero:")

n1 = float(n1)
n2 = float(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2
print("""selecciona con una "S" para si o con una "N" para no:""")
seleccion = "N"
seleccion = input("quieres sumar?:")
if seleccion == "S":
    print("El resultado de la suma es:", suma)
else:
    seleccion = input("quieres restar?:")
    if seleccion == "S":
        print("El resultado de la resta es:", resta)
    else:
        seleccion = input("quieres multiplicar?:")
        if seleccion == "S":
            print("El resultado de la multiplicacion es:", multi)
        else:
            seleccion = input("quieres dividir?:")
            if seleccion == "S":
                 print("El resultado de la división es:", div)
