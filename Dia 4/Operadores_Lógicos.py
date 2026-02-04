    #en Python al igual que en otros lenguajes de programación tenemos los operadores lógicos (and, or, y not)

mi_bool = 4 < 5 < 6 # podemos utilizar los operadores de comparación, pero cuando hacemos evaluaciones más complejas es más conveniente usar los operadores lógicos
print(mi_bool)

mi_bool1 = 4 < 5 > 6 #Por ejemplo en este caso dara como resultado un False, por lo que se necesita el operador "and" para que se pueda realzar la comparación de manera correcta
print(mi_bool1)

    #OPRADOR LÓGICO AND

mi_bool2 = 4 < 5 and 5 > 6 # en este caso ya se puede evaluar las dos condciones y obtenremo un true con and cuando los elementos sean verdaderos
print(mi_bool2)

mi_bool3 = (4 < 5) and 5 == 2 + 3 # con and ya podemos realizar las comprobaciones más complejas
print(mi_bool3)

mi_bool4 = (4 < 5) and (5 == 2 + 3) # en algunas ocaciones se puede poner entre parentecis los elementos a comparar para una mejor visivilidad, pero Python lo interpreta de la misma manera
print(mi_bool4)

mi_bool5 = (55 == 55) and ("perro" == "perro") # Se puede comparar distintos tipos de datos
print(mi_bool5)

    # OPRADOR LÓGICO OR

mi_bool6 = 10 == 10 or 3 == 3 # Con "or" con solo que una condición sea verdadera dará como resultado True
print(mi_bool6)

mi_bool6 = 1 == 10 or 3 == 3 # Por lo que en este caso que solo una condición es verdadera el resusltado siempre será True
print(mi_bool6)

mi_bool7 = 1 == 10 or 3 == 30 #Para que un or de como resultado False las dos condiciones tinen que ser Falsas
print(mi_bool7)

texto = "Esta frase es breve"
mi_bool8 = ('frase' in texto) and ('breve' in texto)
print(mi_bool8)

mi_bool9 = ('frase' in texto) and ('Python' in texto) # con and si solo ua condición es verdadera el resultado será False
print(mi_bool9)

mi_bool10 = ('frase' in texto) or ('Python' in texto) # con or, solo con una condición verdadera será True
print(mi_bool10)

    #OPERADOR LÓGICO NOT
mi_bool11 = not ('a' == 'a') # not es la negación, por lo que el resultado será lo contrario a la evaluación
print(mi_bool11)

mi_bool12 = not ('a' != 'a') # si el resultado de la conparación es un True, con not, pasará a ser False
print(mi_bool12)



