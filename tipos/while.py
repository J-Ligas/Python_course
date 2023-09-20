numero = 1
while numero < 1000000000000000:
    print(numero)
    numero *= 2
    
comando = ""
while comando != "salir":
    comando = input("ingrese salir si quiere terminar el programa:")
    print(comando)
    if comando == "exit": #siempre agregar esta condicional por si llegará a quedar un ciclo infinito de while
        break

