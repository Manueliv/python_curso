mi_bool = 10==25 #Comparación el doble igual (==)
print(mi_bool)

mi_boo2 = 5+5==18-8 #Se puede hacer diferentes tipos de comparaciones, hasta de los resusltados de distintatas operaciones
print(mi_boo2)

mi_bool3 = "blanco" == "negro" #Se pueden conparar hasta string
print(mi_bool3)

mi_bool4 = "blanco" == "blanco" # y efectivamente realiza la comparación y muetra True cuando es verdadero
print(mi_bool4)

mi_bool4 = "blanco" == "Blanco" # La comparación de string es sensible a mayúsculas por lo que esta daria un False
print(mi_bool4)

mi_bool5 = "blanco" == "Blanco".lower()# lo importante es el resultado y no el contenido en sí, por loque si lepasamos lower para hacerlo minuscula ahora si será True
print(mi_bool5)

mi_bool6 = "100" == 100 #si comparamos distintos tipos de datos Python reconoce que no son iguales por lo tanto el resultado será false aunse se vean igual
print(mi_bool6)

mi_bool7 = 100.0 == 100 # Se puede conparar un float con un integer y si el valor es el mismo obtendremos un True, porque el resusltado es el mismo
print(mi_bool7)

mi_bool8 = 100!= 100 #el signo de negación para comprobar si algo es diferente de
print(mi_bool8)

mi_bool9 = 100 != 99 #como con este buscamos diferencia ahora esto sí será un True
print(mi_bool9)

mi_bool10 = 100 > 99 # Los simbolos clásicos de mayor y menor (<,>) funcionan de igaul manera
print(mi_bool10)

mi_bool11 = 5 <= 5 # y asi mismo los signos mayor o igual y menor o igual
print(mi_bool11)

mi_bool12 = 5 >= 6 # si no es ninguna de las dos cosas obtendremos un False
print(mi_bool12)



