"""no hay modulos por importar"""
def suma(a, b):
    """suma"""
    resultado = a + b
    print(resultado)

suma(1, 2)

def suma_2(a, b):
    """suma 2"""
    resultado = a + b
    return resultado


X = suma_2(1, 2)
print(X)
y = suma_2(X, 100)
print(y)
