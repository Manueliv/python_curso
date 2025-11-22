    #DICCIONARIOS
diccionario = {'clave1':'valor1', 'clave2':'valor2'}
print(type(diccionario))
print(diccionario)

#Para acceder a un valor se indica la clave asosiada

resultado = diccionario['clave2']
print(resultado)

cliente = {'nombre':'Juan', 'apellido':'funtes', 'edad':25, 'altura':1.76}
cosnsulta = cliente['apellido'], cliente['nombre']
print(cosnsulta)

diccionario2 = {'clave1':55, 'clave2':[10, 20, 30], 'clave3':{'s1':100, 's2':200}}# no se puede repetir el nombre de una clave, lo marca con line amarilla y aunque funciona solo sale de una
print(diccionario2)

print(diccionario2['clave2']) #para acceder solo a lo que tengamos en la clave 2, que es una lista, recordemos las listas en [] y los diccionarios en {}
print(diccionario2['clave2'][1]) #con este accedera al diccionario2 luego a la clave 2 que es la lista y dentro de la lista al índice 1 que sería 20,

    #Acceder a diccionario que está dentro de un diccionario
print(diccionario2['clave3']) # con esto obtenemos el contenido que está en la clave 3 que es un diciconario dentro del principal

    # para ser más específico y acceder a la clave de un diccionario que está dentro de otro diccionario
print(diccionario2['clave3']['s2'])

    #EJERCICIO
    #de un diccionario que contiene dos claver, en la primera clave una lista las letras a, b, y c, y la segunda clave las letras d, e, y f.
    #imprimir en pantalla la letra "e" en mayuscula (en una sola línea de código)
diccionario3 = {'clave1':['a', 'b', 'c'], 'clave2':['d', 'e', 'f']}
print(diccionario3['clave2'][1].upper())

    #AGREGAR ELEMENTOS A UN DICCIONARIO YA CREADO

diccionario4 ={1:'a', 2:'b'}
print(diccionario4)

diccionario4[3] = 'c' #aqui agregamos la clave 3 entre corchetes con valor 'c' al mismo dicionario
print(diccionario4)

    #Sobreescribir un valor que ya exista

diccionario4[2] = 'B' #del diccionario accedemos a la clave 2 y lo igualamos a su nuevo valor que seria B (b en mayúscula)
print(diccionario4) #como la clave 2 ya existe, no se va a crea una nueva clave dentro del diccionario si no que se va a sobreescribir la que ya existe

    #Ver todas las claves que tiene un diccionario

print(diccionario4.keys()) #para ver las claves que tiene usamos el método keys, solo muestra las clves no los valores
print(diccionario4.values()) #para ver los valores de las claves usamos .values()

    #para ver todos los elementos dl diccionario

print(diccionario4.items()) # con el método items

