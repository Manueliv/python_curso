nombre = "Carina"
print(nombre)
#nombre[0] = "K" # esto dara un error, si queremos acceder al indice cero y cambiarlo por la letra K, ya que los string son inmutables
nombre = "Karina" # aqui estariamos cambiando el contenido de la variable, pero no el string en si
print(nombre)
    #el string Carina no ha cambiado si no  que he creado otro string y he guardado en la variable nombre

n1 = "Kari"
n2 = "na"
print(n1 + n2) #concatenar string con signo +
print(n1 * 5) # si con + concatenamos, con * multiplicamos

poema = """Mil pequeños peces blancos  
como si hirviera 
el color del agua""" #cuando usamos 3 comillas dobles o simples funciona los saltode linea que damos con enter y asi lo mostrara sin dar error
print(poema)    #es otra forma de hacer saltos de linea en strings

print("agua" in poema) # con in podemos recibir un boolean indicando si se encuentra o no el valor el el string true si se encuentra o false si no
print("sol" in poema) #como la palabra sol no se encuntra dara False
print("sol" not in poema) # lo contrario de in, si no esta en el string indica True, si esta dira False, porque seria falso que no esta