nombre = input("Ingrese su nombre: ")
ventas = input("Ingrese sus ventas : ") # aqui se pudo haver indicado directamente que lo se ingrese en el input sea otro tipo de dato ejem: ventas = int(input("")
    #ventas = int(input(Ingrese sus ventas)) (con este codigo pudimos ahorrarnos el paso de convertir el string a int o float obtenido en el input)
venta_convertida_float = float(ventas) #Hacemos la conversion del imput de ventas a float(si no se requiere mucha exaxtitud se pudo indicar convertir a int y no a float)

comision = venta_convertida_float * 13 /100 #guardamos el resultado en la varible comision, (tambien aqui se pudo haber indicado round para aplicar a la varible y y evitar la sigueite linea )
comision_redondeada = round(comision, 2) #ahora ese resultado lo redondeamos indicando como maximo 2 decimales y guardamos en la variable
print(f"Hola {nombre}, este mes ganaste ${comision_redondeada} en comisiones por ventas \"Felicidades\"")