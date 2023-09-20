"""No hay modulo"""
def largo(texto):
    """funcion para contar la longitud de palabras"""
    resultado = 0
    for char in texto:
        resultado += 1
    return resultado #SE UTILIZO EL DEBUGER PARA QUITAR LA INDENTACIÓN
#la indentación o sangría o sangrado hace que el return pare el for y retorne el valor de 1

print("punto de quiebre")
l = largo("Hola mundo")
print(l)
