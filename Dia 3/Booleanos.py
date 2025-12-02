var1 = True #Declaracion de un valor booleno directamente
var2 = False #Recordemos que siempre tiene que ser en mayúscula inicial
print(type(var1))
print(var1)

    #Cración de un boeleano de manera indirecta

numero = 5 > 2+3 #Estamo indicandoque el resultado de esta operación sera booleano
print(type(numero))
print(numero)

numero = 5 == 2+3 #Con doble igual (==), estamos diciendo que es igual, no es una asiganción como en las variables
print(type(numero))
print(numero)

 #con los demás signos de comparación podemos realizar diferentes comprobaciones y el resultado será un booleano True o false
 #>= sería mayor o igual, != difrente de

numero2 = bool(5>6) #Podemos indicar directamente que es un booleano
print(numero2)

numero3 = bool(5<6) #No es necesario que usemos la palabra 'bool', pero se debe conocer porque se verá de diferentes códigos
print(numero3)

numero4 = bool() #Si queremos generar un valor False, dejamos los parentecis sin datos
print(numero4)

lista = [1,2,3,4] #Construir un valor booleano
control = 5 in lista #Aqui preguntamos si 5 esta en lista, Como  no esta e resultado será False
print(type(control))
print(control)

lista = [1,2,3,4] #Construir un valor booleano
control = 5 not in lista #Aqui estamos indicando que 5 no esta(not in) lista, como es correcto imprimirá True
print(type(control))
print(control)
