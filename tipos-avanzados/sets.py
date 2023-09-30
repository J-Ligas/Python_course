#set sirve para tener numeros no repetidos
primer = {1, 1, 2, 3, 3, 4, 5}
print(primer)
primer.add(6)
primer.remove(1)
print(primer)
#crear un set en base a una lista
lista = [ 3, 3, 4, 5]
print(lista)
segundo = set(lista)
print(segundo)
#operador de intersección "&"
print("intersección")
print(primer & segundo)
#diferencia 
print("diferencia")
print(primer - segundo)
#diferencia simetrica
print("diferencia simetrica")
print(primer ^ segundo)
print("union")
print(primer | segundo)
#con los sets no se pueden consultar por indice
#set[0] marcaría error
#podemos preguntar if 5 in set print(si está el 5)
