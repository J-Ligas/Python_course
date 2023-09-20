def suma(*numeros): #parametros iterables
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2,1,3)
suma(2,1,3,4,5,6,7,8,9,19)
suma(2,1,3,98214792,892134792384)