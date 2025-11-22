    #TUPLES
mi_tuple = (1, 2, 3, 4)
print(mi_tuple)

t = (5, 5.6, 'fff') # un tuple puede conter diferentes tipos de elementos, como vemos int, float, strin pero también listas, diccionarios y otros taples
print(t)

print(mi_tuple[0]) #para cosultar los elementos de un tuple es igual que con las listas
print(mi_tuple[-2]) # con numeros negativos se empieza a contar de derecha a izquierda, igual nuvamente que las listas

    #los taplues al igual que los string son inmutables por lo que no podemos cambiar un elemento que este dentro del tuples, para eso se tendria que crea una nueva variable
    # por lo tanto este codigo: mi_tuple[0] = 5, indicaria un error, al querer asignar al elemento de índice o el número 5

    #ANIDAR TUPLES

mi_tuple2 = (1, 2, (10, 20), 4) # en este tuple en la posisción 2 ponemos otro tuple
print(mi_tuple2[2]) # consultamos, indicando imprimir el tuple, luego la posisión de su índice nos mostrara el tuple omas el bien contedino que sería (10, 20)
print(mi_tuple2[2][0])# para ser más específico al igual que con listas y los diccionarios, se indica el índice del taple y del taple dentro

    #Podemos pasar un taple a un alista y viceversa

mi_tuple = list(mi_tuple) #taple pasado a lista
print(type(mi_tuple))

mi_tuple = tuple(mi_tuple) #volvemos a pasar el taple convertid a lista a un taple nuevamente
print(type(mi_tuple))

    #También se puede asignar el contenido de un taple a diferentes variables

t = (1, 2, 3 )
x, y, z = t # Esto solo se puede hacer cuanto se tiene la misma cantidad de valores dentro del tuple que de variables, si fura catidad distinta dara error
print(x, y, z) # Esto se puede realizar con las listas y con los diccionarios, siempre que se tenga la misma cantidad de valores y variables
print(y)

taple2 = (1, 2, 3, 1)
print(len(taple2)) # podemos usar len para conocer el largo o cantidad de elementos del tuple, asi como en listas y diccionarios
print(taple2.count(1)) # para contar cuantas veces se encuntra ese elemento delntro del tuple
print(taple2.index(2)) # para consusltar en que índice se encuentra un valor

    #Los tuples no son objetos de uso común peor es bueno conocerlos, ya que tiene su uso espefico como cuando no se quiere que cambie los valores, ya que son inmutables


