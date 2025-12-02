    #LISTAS
mi_lista = ["a", "b", "c"] #las listas en python van dentro de corchetes
print(type(mi_lista))

otra_lista = ['hola', 55, 6.1] #las listas en python pueden conter diferentes tipos de elementos
print(type(otra_lista))

resultado = len(mi_lista) #propiedad len, para contar el número de elementos
print(resultado)

resultado_02 = mi_lista[0]# accedemos al índice cero de la lista, que sería la letra a
print(resultado_02)

resultado_03 = mi_lista[0:2] #para ver el elemento desde índice cero hasta el 2 sin incluir este último, por lo tanto, sería índice 0 y 1 oséa a y b respectivamente
print(resultado_03)

resultado_04 = mi_lista[0:] #si no se pone nada dentro de los corchetes dara invalid syntax, si ponemos cero y dos puntos (0:) mostrará todos los elementos de la lista
print(resultado_04)

    #CONCATENACION DE LISTAS

mi_lista2 = ["d", "e", "f"]
print(mi_lista + mi_lista2)

print(mi_lista)
print(mi_lista2)  #las listas principales siguen existiendo individualmente

    # si quisieramos una sola lista con los elementos de las dos, tendriamos que crear una tercera variable y ahi indicar que serían los eleentos de las dos listas
mi_lista3 = mi_lista + mi_lista2
print(mi_lista3)

    #MODIFICACION DE LISTAS
    #a diferencia de los string los elementos de las listas no son inmutables osea si se pueden modificar

mi_lista3[0] = 'alfa' #en la variable mi_lista3 accedemos al indice cero e indicamos que lo camiamor por alfa
print(mi_lista3) #como resultado obtendremos que ahora el inice cero ya no es la letra 'a' si no la palabra 'alfa'

   #METODOS DE LAS LISTAS
    #AGREGAR ELEMENTOS A LAS LISTAS

mi_lista3.append('g') # con el metodo append, agregamos elementos a las listas al final, aquí la lista de origen fue modificada sin necesidad de crear otra varible como con string
print(mi_lista3)

mi_lista3.pop() #con el método pop si se deja sin parametro dentro de parentecis  inidicamos que se elimine el ultino elemento de la lista
print(mi_lista3)

mi_lista3.pop(0) #si dentro parentecis ponemos el índice, eliminamos el elemento repectivo
print(mi_lista3)
print(mi_lista3[0])
print(mi_lista3[1])
print(mi_lista3[2])

    #Por si queremos almacenar el elemento eliminado para manipularlo o utilizarlo

eliminado = mi_lista3.pop(0) #lo almacenamos en una nueva variable
print(eliminado)

    #MÉTODO SORT
    #El métod sort sirve para ordenar los elementos de una lista

lista = ['g', 'o', 'b', 'm', 'c']
lista.sort() # sin parametros dentro del parentecis ordena en orden alfabetico las letras y palabras y en orden ascendete si fueran números
print(lista)

    #sort no devuelve nada, por lo que diferencia de otros métods no los podemos utilizar en una variable, osea no se podria: varivable = lista.sort()

    #MÉTODO REVERSE

lista.reverse()# el método reverse da vuelta al orden, pone lo ultimo de primero y lo primero de ultimo
print(lista) #y al igual que sort reverse no devuelve nada y no lo podemos almacenar direcctamente en una variable porque no daria el objeto none
