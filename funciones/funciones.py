def hola(): #dentro del parentesis van los parametros
    print("hola mundo")
    print("hola user")

#Dejar 2 espacios después de una función
hola() #dentro del parentesis van los argumentos que yo quiera asignar
hola()

def hola(nombre): #con argumento
    print("hola", nombre)

#Dejar 2 espacios después de una función
hola("Juan")
hola("Lalo")

def hola(nombre, apellido): #con argumento
    print("hola", nombre, apellido)

#Dejar 2 espacios después de una función
hola("Juan", "Ramirez")
hola("Lalo", "Contreras")

def hola(nombre, apellido="Feliz"): #con argumento default en apellido
    print("hola", nombre, apellido)

#Dejar 2 espacios después de una función
hola("Juan", "Ramirez")
hola("Lalo")

#argumentos nombrados
def hola(nombre, apellido="Feliz"): #con argumento default en apellido
    print("hola", nombre, apellido)

#Dejar 2 espacios después de una función
hola(apellido="Juan",nombre="Ramirez")
hola(nombre="Lalo")