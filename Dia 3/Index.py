mi_texto = "Esta es una prueba"
resultado = mi_texto[0] #motraria lo que haya en el índice cero de la variable "mi_texto"
print(resultado)

resultado_02 = mi_texto[9] #mostrará el elemento del índice que en este caso es la letra n
print(resultado_02)

resultado_03 = mi_texto[-4] #cuando se le indica números negativos el primer elemento está en la posiscion cero, pero luego comienza contar de derecha isquierda
print(resultado_03)

resultado_04 = mi_texto.index("n") #con el metodo index nos muetra en que índice se encuetra el caracter que indiquemos, en este caso la letra ene en el 9
print(resultado_04)

#resultado_05 = mi_texto.index("x") #si indicamos un caracter que no esta en la cadena obtendiramos un error: substrinf no found
#print(resultado_05)

resultado_06 = mi_texto.index("prueba") # si indicamos una palabra entera nos muestra el número de índice donde comienza la palabra
print(resultado_06)
    #Si la palabra buscada con index, esta aml escrita también indicara un error al no encontrarla
    #también es sensible a mayusculas y minusculas, por lo que si buscamos Prueba y no prueba, también dara error

resultado_07 = mi_texto.index("a") # si buscamos un caracter que se encuentre varias veces en la cadena, solo mostrara el indice del primero que encuentre
print(resultado_07)
    #index solo busca de izquierda a dereca y se detiene en el primer resultado que encuentra

resultado_08 = mi_texto.index("a", 5) # con el segundo parametro se indica desde donde comenzara a buscar la letra
print(resultado_08)

#resultado_09 = mi_texto.index("a", 5, 10) # Con el trecer parametro indicamos hasta donde buscara, pero no incluye ese último valor
#print(resultado_09)     #Por lo que en este caso daria un error, ya que laletra a del índice 10 no la tomaria en cuenta

resultado_10 = mi_texto.rindex("a") #con rindex comienza a buscar de derecha a izquierda, por lo que encontra la ultima letra "a" y nos mostrara su indice
print(resultado_10)

