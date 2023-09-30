#crear una lista de números
numeros = [1, 2, 3, 4]
letras = ["a", "b", "c", "d"]
palabras = ["curso", "de", "python"]
palabras_random = ["Hola", "adios", "curso", "programación"]
print(numeros)
print(letras)
print(palabras)
print(palabras_random)
#crear lista con boleanos
boleanos = [True, False, True, True]
print(boleanos)
#crear una matriz
matriz = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(matriz)
#crear una lista de 100 elementos
cien_ceros = [0] * 100
print(cien_ceros)
#crear una lista de 1000 elementos pares
mil_ceros_unos = [0, 1] * 1000
print(mil_ceros_unos)
#sumar listas
suma_lista = numeros + letras
print(suma_lista)
#crear lista numerada desde el 0
crear_lista_range = list(range(10))
print(crear_lista_range)
#crear una lista numerada con range desde 1 hasta 11, solo muestra hasta el 10
crear_lista_range_2 = list(range(1, 11))
print(crear_lista_range_2)
#imprimir un strinng con una lista
caracter = list("hola mundo")
print(caracter)
