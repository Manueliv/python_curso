texto_usuario = input("Ingrese su texto: ")
letra1 = input("Ingrese 3 letras a su elección, ingrese la primera letra: ")
letra2 = input("Ingrese la segunda letra: ")
letra3 = input("Ingrese la tercera letra: ")

    #1- CONTAR CUANTAS VECES APARECEN LAS LETRAS EN LA FRASE INGRESADA
ingreso_list = list(texto_usuario) #Pasando el string del input a lista
minusculas_frase = texto_usuario.lower() #convirtiendo de la frase a minusculas
letra1 = letra1.lower() #convirtiendo las letras a minusculas
letra2 = letra2.lower()
letra3 = letra3.lower()
print("se imprime lo que esta en minusculas: ",minusculas_frase)
print(type(ingreso_list)) #para comprobar que el texto ya sea de tipo lista
print(f"La letra \"{letra1}\" aparece " , minusculas_frase.count(letra1), "veces,", f"la letra \"{letra2}\" aparece" , minusculas_frase.count(letra2), "veces,", f" y la letra \"{letra3}\" aparece ",minusculas_frase.count(letra3),"veces") #Para contar cuatas veces se encuntra la letra ingresada en la frase

    #2- DECIR CUANTAS PALABRAS HAY EN EL TEXTO INGRESADO
contar_palabras = texto_usuario.split() # Con split dividividmos la cadena según un caracter especial que por defecto es el espacio
print(contar_palabras)
print("El número de palabras que tiene la frase es: " ,len(contar_palabras)) #Con len para contar el número de palabras dentro de la lista

    #3- INFORMAR CUAL ES LA PRIMERA LETRA Y LA úLTIMA DE LA FRASE INGRESADA
primera_letra = texto_usuario[0] #para acceder al primer elemento de la lista
print("La primera letra de la frase es: ",primera_letra)
ultima_letra = texto_usuario[-1] #para acceder al último elemento de la lista
print("La ultima letra de la frase es: ",ultima_letra)

    #MOSTRAR COMO QUEDARIA EL TEXTO SI INVIRTIERAMOS EL ORDEN DE LAS PALABRAS

contar_palabras.reverse() #para invertir el orden de los elementos de la lista usamos reverse
contar_palabras = " ".join(contar_palabras) #Para unir los elementos de la lista usamos join, pero primero ponemos un espacio entre comillas que será el separador de las palabras
print(contar_palabras)

    #DECIR SI UNA PALABRA ESPECIFICA SE ENCUENTRA DENTRO DEL TEXTO, EN ESTE CASO (LA PALABRA PYTHON)
encontrar = "python" in contar_palabras.lower() #Para guardar en la variable 'encontrar' la respuesta booleana de la comprobacion si se encutra la palabra 'Python'
print(encontrar) #Para comprobar que efectivamente en la variable encontrar se encuentre el resultado booleano obtenido de la operacion anterior
#print("python" in contar_palabras.lower())
diccionario = {'clave':encontrar} #Creamos el diccionario asignando a la clave el valor booleano de True sin comillas solo pasamos la variable donde está el valor
resultado = diccionario['clave'] #asiganamos a la varibble resusltado el valor del diccionario almacenado en clave
print("La respuesta a si se encuentra la palabra python en la frase es: ", resultado)





