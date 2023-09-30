#manipular listas
mascotas = ["pelusa", "firulais", "chachito"]
print(mascotas)
#acceder al elemento 0 de la lista
print(mascotas[0])
#cambiar el valor de un elemento en una lista
mascotas[0] = "chuchito"
print(mascotas)
#acceder a rango de lista
#de inicio a final
print(mascotas[:])
#de inicio hasta el 1
print(mascotas[:1])
#desde el 1 hasta el final
print(mascotas[1:])
#desde el 1 hasta el 2
print(mascotas[1:2])
#ir al último
print(mascotas[-1])
#ir al penúltimo
print(mascotas[-2])
numeros_2 = list(range(1, 22))
#ir a solo pares desde el 0
print(numeros_2[::2])
#ir a solo impares iniciando en 1
print(numeros_2[1::2])
#ir de 3 en 3 desde el 2 y que solo llegue hasta el idnice 15
print(numeros_2[2:15:3])
