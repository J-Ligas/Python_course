#desempaquetado
numeros = [1, 2, 3]
#lo que se dscribe a continuación no se recomienda hacer
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]
# se recomienda la siguiente opción
# primero, segundo, tercero = numeros
# print(primero)
# print(segundo)
# print(tercero)
numeros_2 = list(range(1,11))
#desempaquetando el primer número y empaquetando al resto en *otros
primero, *otros = numeros_2
print(primero)
#desempaquetando el primer número y al último empaquetando al resto en *otros
primero, *otros, ultimo = numeros_2
print(primero, ultimo)
#desempaquetando el primer número y al segundo empaquetando al resto en *otros
primero, segundo, *otros = numeros_2
print(primero, segundo)
