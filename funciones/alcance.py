"""No hay modulo por importar"""
#esta es una variable global y no es local como la de las funciones
#utilizar variables globales es una mala practica
#si se quiere utilizar una variable global dentro de una funcion utilizar 
#"global" antes de mencionarla, pero esto no se recomienda
# no se deben mezclar variables globales y locales porque es 
#facil cometer errores y dificil de encontrarlos
SALUDOS = "Hola"
"""No hay modulo por importar"""
def saludar():
    """funcion para saludar"""
    saludo = "Hola" #la variable saludo solo tiene alcance en la funcion saludar, fuera de ahí no
    print(saludo)

def saludo_persona():
    """funcion para saludar personas"""
    saludo = "Hola persona"
    print(saludo)

saludar()
saludo_persona()
#las variables de saludo en las dos fucniones son
#totalmente diferentes, no son variables de contexto global
