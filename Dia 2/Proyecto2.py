nombre = input("Ingrese su nombre: ")
ventas = input("Ingrese sus ventas : ")

venta_convertida_float = float(ventas) #Hacemos la conversion del imput de ventas a float

comision = venta_convertida_float * 13 /100 #guardamos el resultado en la varible comision
comision_redondeada = round(comision, 2) #ahora ese resultado lo redondeamos indicando como maximo 2 decimales y guradmos en la variable
print(f"Hola {nombre}, este mes ganaste ${comision_redondeada} en comisiones por ventas \"Felicidades\"")