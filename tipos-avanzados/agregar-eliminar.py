#agregar y eliminar elementos de una lista
mas_1 = ["perro", "gato", "ave", "leon", "elefante", "jirafa",
         "dragon", "leon", "elefante", "jirafa", "dragon", "leon",
         "elefante", "jirafa", "dragon"]
print(mas_1)
#inserta "miaumiau en el indice 1 de la lista"
mas_1.insert(1,"miaumiau")
print(mas_1)
#inserta "miaumiau al final de la lista"
mas_1.append("miaumiau")
print(mas_1)
#elimina el elemento indicado de la lista pero solo lo hace una sola vez
mas_1.remove("dragon")
print(mas_1)
#eliminar el último elemento de una lista
mas_1.pop()
print(mas_1)
#eliminar el elemento seleccionado con su indice en una lista
mas_1.pop(1)
print(mas_1)
#eliminar un elemento de una lista con su indice
del mas_1[0]
print(mas_1)
mas_1.clear()
print(mas_1)
