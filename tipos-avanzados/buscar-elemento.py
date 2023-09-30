#buscar elementos
mascotas = ["perro", "gato", "ave", "leon", "elefante", "jirafa", "dragon"]
print(mascotas.index("dragon"))
#devuelve el indice de la lista si el elemento se encuentra
if "perro" in mascotas:
    print(mascotas.index("perro"))
#si no existe no imprime nada
if "lagarto" in mascotas:
    print(mascotas.index("lagarto"))
#si hay elementos repetidos se pueden contar
mas_1 = ["perro", "gato", "ave", "leon", "elefante", "jirafa",
         "dragon", "leon", "elefante", "jirafa", "dragon", "leon",
         "elefante", "jirafa", "dragon"]
print(mas_1.count("dragon"))
