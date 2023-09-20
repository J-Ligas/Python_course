"""Se tiene que colocar información sobre el modulo justo arriba de la importacion"""
def hola():
    """Aquí se menciona info sobre al función; dentro del parentesis van los parametros"""
    print("hola mundo")
    print("hola user")

#Dejar 2 espacios después de una función
hola() #dentro del parentesis van los argumentos que yo quiera asignar
hola()

def hola_1(nombre):
    """con argumento"""
    print("hola", nombre)

#Dejar 2 espacios después de una función
hola_1("Juan")
hola_1("Lalo")

def hola_2(nombre, apellido):
    """con argumento"""
    print("hola", nombre, apellido)

#Dejar 2 espacios después de una función
hola_2("Juan", "Ramirez")
hola_2("Lalo", "Contreras")

def hola_3(nombre, apellido="Feliz"):
    """con argumento default en apellido"""
    print("hola", nombre, apellido)

#Dejar 2 espacios después de una función
hola_3("Juan", "Ramirez")
hola_3("Lalo")

#argumentos nombrados
def hola_4(nombre, apellido="Feliz"):
    """con argumento default en apellido"""
    print("hola", nombre, apellido)

#Dejar 2 espacios después de una función
hola_4(apellido="Juan",nombre="Ramirez")
hola_4(nombre="Lalo")

#argumentos nombrados
def hola_5(nombre="Carlos", apellido="Feliz"):
    """con argumento default en apellido"""
    print("hola", nombre, apellido)

#Dejar 2 espacios después de una función
hola_5(apellido="Juan",nombre="Ramirez")
hola_5()
