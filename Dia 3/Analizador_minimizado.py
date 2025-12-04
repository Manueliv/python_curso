texto_usuario = input("Ingrese su texto: ")
letra1 = input("Ingrese 3 letras a su elección, ingrese la primera letra: ")
letra2 = input("Ingrese la segunda letra: ")
letra3 = input("Ingrese la tercera letra: ")

    #1- CONTAR CUANTAS VECES APARECEN LAS LETRAS EN LA FRASE INGRESADA
ingreso_list = list(texto_usuario)
minusculas_frase = texto_usuario.lower()
letra1 = letra1.lower()
letra2 = letra2.lower()
letra3 = letra3.lower()
print(f"La letra \"{letra1}\" aparece " , minusculas_frase.count(letra1), "veces,", f"la letra \"{letra2}\" aparece" , minusculas_frase.count(letra2), "veces,", f" y la letra \"{letra3}\" aparece ",minusculas_frase.count(letra3),"veces")

    #2- DECIR CUANTAS PALABRAS HAY EN EL TEXTO INGRESADO
contar_palabras = texto_usuario.split()
print(contar_palabras)
print("El número de palabras que tiene la frase es: " ,len(contar_palabras))

    #3- INFORMAR CUAL ES LA PRIMERA LETRA Y LA úLTIMA DE LA FRASE INGRESADA
primera_letra = texto_usuario[0]
print("La primera letra de la frase es: ",primera_letra)
ultima_letra = texto_usuario[-1]
print("La ultima letra de la frase es: ",ultima_letra)

    #MOSTRAR COMO QUEDARIA EL TEXTO SI INVIRTIERAMOS EL ORDEN DE LAS PALABRAS
contar_palabras.reverse()
contar_palabras = " ".join(contar_palabras)
print(contar_palabras)

    #DECIR SI UNA PALABRA ESPECIFICA SE ENCUENTRA DENTRO DEL TEXTO, EN ESTE CASO (LA PALABRA PYTHON)
encontrar = "python" in contar_palabras.lower()
print(encontrar)
diccionario = {'clave':encontrar}
resultado = diccionario['clave']
print("La respuesta a si se encuentra la palabra python en la frase es: ", resultado)