#extraer datos de una lista
usuarios = [["juan", 3], ["ramon", 8], ["carlos", 4], ["pedro", 2]]

nombres = []
for usuario in usuarios:
    nombres.append(usuario[0])
print(nombres)

#tambien se puede filtrar y modificar una lista así:
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres)
