texto = "ABCDEFGHIJKLM"
fragmento = texto[2] #el metodo para obtener caractes de una cadena y guardarlo en una variable se llama slicing (rebanar), y se usa con []
print(fragmento)

    #VARIACIONES

fragmento_2 = texto[2:5] #con ':' (dos puntos) y el segundo parametro indicamamos hasta donde se obtendrar los caracteres, pero sin tomar en cuenta ese último
print(fragmento_2)

fragmento_3 = texto[2:] #se se omite el parametro despues de los dos puntos se obtiene hasta el final de la cadena
print(fragmento_3)

fragmento_4 = texto[:5] #si se omite el primero se obtiene desde el inicio haste el índice del parametro que indicamos después de los ':' pero sin tomarlo en cuenta
print(fragmento_4)

fragmento_5 = texto[2:10:2]# de indíca desde donde comienza a obtener, hasta dode termina, y el untimo parametro indica cada cuantos irá obteniendo
print(fragmento_5)          #con ese último parametro tomará un caracter y se saltará otro hasta llegar el utlimo índice indicado

fragmento_6 = texto[::-1] #con esto indicamos a python que devuelva toda la cadena, pero en orden inverso, si indicamos -2 también será en orden inverso pero saltandose uno
print(fragmento_6)
