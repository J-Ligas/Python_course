animal = "  Elefante gris  " #Agregue dos espacios antes y después para observar la propiedad de strip
print(animal.upper()) #Mayus
print(animal.lower()) #minusculas
print(animal.capitalize()) #Primera en mayus
print(animal.title()) #Primera de cada palabra en mayus
print(animal.strip()) #Eliminar espacios antes y después del contenido del string
print(animal.upper().strip()) #Combinación de métodos o funciones
print(animal.upper().rstrip()) #Eliminación de espacios de la derecha (sangría)
print(animal.upper().lstrip()) #Eliminación de espacios de la izquierda (sangría)
print(animal.find("e")) #Buscar cadena de caracteres y devuelve el indice
print(animal.find("Z")) #Buscar cadena de caracteres y devuelve el indice -1 si no existe
print(animal.replace("e", "J")) #remplaza las "e" por las "j", si no encuentra no hace nada...
print("Ele" in animal) #Busca "Ele" en el string y devuelve boleano True
print("ElJ" in animal) #Busca "ElJ" en el string y devuelve boleano False porque .remplace no modifica el valor de la variable
print("Y" not in animal) #Devuelve True por usar una negación con "not" el False
