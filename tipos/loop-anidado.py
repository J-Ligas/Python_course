for j in range(3):
    for k in range(2):
        print(f" {j}, {k}") #tratar de evitar for en for
 
resultado = input("escribe el salir con mayusculas y minusculas:")
if resultado.lower() == "salir":
    print("verificacion para mayusculas y minisculas exitosa")
