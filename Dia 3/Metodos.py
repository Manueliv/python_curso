texto = "Este es el texto de Manuel"

resultado = texto.upper() #upper para hacer mayusculas
print(resultado)

resultado01 = texto[2].upper() #Solo para mostrar el elemento de índice indicado en mayusculas
print(resultado01)

resultado02 = texto.lower()# pasar a minusculas
print(resultado02)

resultado03 = texto.split() #Separar elementos en una lista
print(resultado03)

resultado04 = texto.split("t") # si indicamos un parametro en parentecis ese será el separador para los grupos de caracteres
print(resultado04)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d]) #Si indicamos join con signo más (a+b+c+d), unira letra mas el separador, si es [] dentro de parentecis, palabras por palabra

print(e)

resultado05 = texto.find("g") #La diferencia con index que con find si no se encuentra el elemento muestra -1 y no da error como con index
print(resultado05) # si el elemento existe muestra en índice donde se encuentra, si no está muestra -1
    # asi mismo se puede buscar palabras exactas y muestra el índice donde se encutra la primera letra de esa palabra

resultado06 = texto.replace("Manuel",  "Todos") # repleace necesita dos parametros, el primero indica el elemento a reemplazar y el segundo con que  lo vamos a reemplazar
print(resultado06)

resultado07 = texto.replace("e", "x") #se puede remplazar cualquier elemento ya sea palabras o como en este caso letra, la e por la x
print(resultado07)

