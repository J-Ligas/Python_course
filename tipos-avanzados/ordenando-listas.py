#ordenar
numeros = [1, 23, 54, 2, 5, 23, 343, 43436, 324, 675]
#ordena pero modifica la lista existente
# numeros.sort()
# print(numeros)
# numeros.sort(reverse=True)
print(numeros)
#sorted crea una nueva lista y no modifica la lista original de "numeros"
numeros_2 = sorted(numeros)
print(numeros_2)
#ordenar listas en listas con un idnice al inicio (esto no funciona si no hay indice al inicio)
usuarios = [[4, "Luis"], [2, "Pedro"], [3, "Juan"]]
print(usuarios)
usuarios.sort()
print(usuarios)
 # Si cambiamos el orden del indice entonces se ncesita relizar una funcion
usuarios = [["Luis", 4], ["Pedro", 2], ["Juan", 3]]
print(usuarios)
#no se necesita importar nada
def ordena(elemento):
    #sirve para ordenar los elementos de la lista por su indice que esta en la posicion 1
    return elemento[1]
#ordena por si solo no acepta los indices necesita el nombre del elemento 
usuarios.sort(key=ordena)
print(usuarios)
#ahora al revés
usuarios.sort(key=ordena, reverse=True)
print(usuarios)

#si la función solamente se utiliza una sola vez entonces se puede utilizar la función lambda
usuarios.sort(key=lambda el:el[1], reverse=True)
print(usuarios)
