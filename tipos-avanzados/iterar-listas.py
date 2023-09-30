#iterar listas en ciclos for
mascotas = ["perro", "gato", "ave", "leon", "elefante", "jirafa", "dragon"]
#iterar cada mascota
for mascota in mascotas:
    print(mascota)
#iterar cada indice de mascota; devuelve una tupla con el idnice y la mascota (0, "perro")...
for mascota in enumerate(mascotas):
    print(mascota)
#iterar cada indice de mascota; devuelve una tupla con el idnice y la mascota (0, "perro")...
for mascota in enumerate(mascotas):
    print(mascota[0]) #Se puede acceder a los indices de la tupla
#iterar cada indice de mascota; devuelve una tupla con el idnice y la mascota (0, "perro")...
for mascota in enumerate(mascotas):
    print(mascota[1]) #Se puede acceder a los indices de la tupla