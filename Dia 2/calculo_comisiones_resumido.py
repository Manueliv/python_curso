nombre = input("Ingrese su nombre: ")
ventas = float(input("Ingrese sus ventas : "))

comision = round(ventas* 13 /100 , 2)
print(f"Hola {nombre}, este mes ganaste ${comision} en comisiones por ventas \"Felicidades\"")