#diccionarios
punto = {"x" : 25, "y" : 50}
print(punto)
print(punto["x"])
punto["z"] = 75
print(punto)
print(punto.get("x"))
#si el argumento no existe devolvera un "none"
del punto["x"]
print(punto)
#iterar llaves
for valor in punto:
    print(valor)
#iterar valores y llaves
for valor in punto:
    print(valor, punto[valor])
#iterar valores de las llaves
for valor in punto:
    print(punto[valor])
#desempaquetamiento de diccionarios
punto_1 = {"x" : 1,"y" : 2}
print(punto_1)
punto_2 = {"w" : 3,"v" : 4}
print(punto_2)
combinado = {**punto_1, **punto_2, "Z" : 45}
print(combinado)


