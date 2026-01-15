if 10 > 9: #Con if se evalua si lo qye esta es true o False, si es true ejecuta el código siguiente
    print("Es correcto")


if True: # Por lo, tanto esto ejecutará el código siguiente
    print("Es correcto")


x = True #Usando una variable, basicamente if ejecuta el código indicado si es True

if x:
    print("Es correcto")

if 5 == 2:
    print("Es correcto")
else: #Con "else" indicamos el código que se deverá ejecutar cuanto la condición no sea verdadera
    print("No es correcto")

mascota = "pez"

if mascota == "gato":
    print("Tienes un gato")
elif mascota == "perro": #con elif indicamos el códio que se debe ejecutar si no se cumple la primera condición
    print("Tienes un perro")
elif mascota == "pez": #se puede anidar tantos elif como sea necesario
    print("Tienes un pez")
else:
    print("No se que mascota tienes")#con el else se ejecuta si ninguna condición anterior se cumple

#ANIDAR CONDICIONES if

edad = 16
calificacion = 9

if edad < 18:
    print("Eres menor  edad")
    if calificacion >= 7:
        print("Aprobado")
    else:
        print("No aprobado")
else:
    print("Eres mayor edad")



