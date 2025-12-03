mi_set = set([1, 2, 3, 4, 5]) #primera forma de escribir un set la palabra set([]), los corchetes pueden ser llaves {} y funcionria igual
print(type(mi_set))
print(mi_set)

otro_set = {1, 2, 3} #segunda forma de escribir un set usando llaves solamente {}, y más práctica
print(type(otro_set))
print(otro_set)

    #los sets no se pueden bucar elementos como en las listas o diccionarios
    #Los sets son elementos unicos, por lo tanto, no pueden tener repeticiones

#se sets agregan elementos repetidos a set, simplemente se ignoran

print(len(mi_set)) #en los sets funciona la propiedad len, para saber la cantidad de elementos que contiene

print(2 in mi_set) # tanmbien la propiedad in, para saber si ese elemento está dentro del set, indicará un "True"

    #UNION DE SETS

s1 = {1, 2 ,3}
s2 = {3, 4, 5}
s3 = s1.union(s2) # Con el método "union" unidomos dos set en uno solo y si hay elementos comunes solo queda uno en el set resultante
print(s3)

    #AGREGAR ELEMENTOS AL SET
s1.add(4) #con el método "add" agregamos elementos, si se intenta agregar un elemento que ya existe no da error, pero no lo agrega
print(s1)

    #ELIMINAR ELEMENTOS DE UN SET

s1.remove(3) # Con remove elemianmos elementos del set, si intentamos eliminar elementos que no existes dara un error
print(s1)

s1.discard(6)  # con discard también se eliminan elementos, con la diferencia que si no existen no da ningun error
print(s1)

s1.pop() #con por hay que tener cuidado, ya que eliminara un elemento aleatorio
print(s1)

    #pop muy útil si se quisiera hacer un sorteo

s1.add(6)
print(s1)
sorteo = s1.pop() #Recordemos que pop devuelve un elemento aleatorio, por lo que puede deolver cualquier elemento del set
print(sorteo) #con esto mostrará el número eliminaod aleatoramente

print(s1) # volvemos a imprimir el set para revisar los elementos que han quedado despúes de uitilizar .pop

s1.clear() #con clear si se deja sin argumentos deja completamente vacio el set
print(s1)









