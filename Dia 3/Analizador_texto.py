texto_usuario = input("Ingrese su texto: ")
letra1 = input("Ingrese 3 letras a su elección, ingrese la primera letra: ")
letra2 = input("Ingrese la segunda letra: ")
letra3 = input("Ingrese la terceira letra: ")

    #1- CONTAR CUANTAS VECES APARECEN LAS LETRAS EN LA FRASE INRESADA
ingreso_list = list(texto_usuario) #Pasando el string del input a lista
minusculas = texto_usuario.lower(), letra1, letra2, letra3 #convirtiendo los textos a minusculas
print(type(ingreso_list)) #para comprobar que el texto ya sea de tipo lista
print(f"La letra \"{letra1}\" aparece " , ingreso_list.count(letra1), "veces,", f"la letra \"{letra2}\" aparece" , ingreso_list.count(letra2), "veces,", f" y la letra \"{letra3}\" aparece ",ingreso_list.count(letra3),"veces") #Para contar cuatas veces se encuntra la letra ingresada en la frase

    #2- DECIR CUANTAS PALABRAS HAY EN EL TEXTO INGRESADO
contar_palabras = texto_usuario.split() # Con split dividividmos la cadena según un caracter especial que por defecto es el espacio
print(contar_palabras)
print("El número de palabras que tiene la frase es: " ,len(contar_palabras)) #Con len para contar el número de palabras dentro de la lista

    #3- INFORMAR CUAL ES LA PRIMERA LETRA Y LA úLTIMA DE LA FRASE INGRESADA
primera_letra = texto_usuario[0]
print("La primera letra de la frase es: ",primera_letra)
ultima_letra = texto_usuario[-1]
print("La ultima letra de la frase es: ",ultima_letra)




