edad = input("Ingresa te edad ") # utilizamos input para solicitar dadots al usuario
print(edad)
print(type(edad)) # lo que se ingresa con input su tipo de dato sera siempre string

conver = int(edad) # con igualar la variale a int indicamos que a ese tipo de dato queremos convertir
print (type(conver)) # Utulizamos type dentro de un print para ver el tipo de dato ya convertido

nueva_edad = conver + 1 # ahora que ya está convertido la edad a int y guardado en la variable conver ya podemos sumar
print(nueva_edad)

