print(round(90/7)) # utlizando  roud para redondear el resusltado de la divicion 90/7

resultado = round(90/7) # aquí guardamos el resultado del redonde en una variable.
print(resultado)

resultado1 = 90/7 # en esta forma aqui solo hacemas la divicion
redondeo = round(resultado1) # Luego a ese resusltado le aplicamos round para redondear
print(redondeo) # finalmente imprimimos utilizando la variable donde guadamos el resultado ya redondedado

valor0 = round(95.6666666666666, 2) #en este caso aplicamos round en el resultado guardado en la variable e indicamos los decimales deseados(2)
print(valor0)
print(type(valor0))#podemos ve el tipo de dato obtenido y al ser sin decimales se ha convertod en int

valor = round(95.6666666666666,) #en este caso aplicamos round en el resultado guardado en la variable
print(valor)
print(type(valor))#podemos ve el tipo de dato obtenido y al ser sin decimales se ha convertod en int

valor1 = 95.66666666666  # en este caso en la variable solo se almacena el resusltado
print(round(valor1)) # y en la impresion se indica el round para mostrar el resusltado
print(type(valor1)) #mostrara float aunque el resutado es el mismo, porque solo se aplica el roun en la forma de mostrar
    #si el round lo aplicamos en la varible si cambia el tipo de dato, pere si  solo es en el print no ya que solo seria para mostrar

