# formatear se llama cuando en un print utilizamos cadenas más varias de diferente valor para mostrar
color = "rojo"
matricula = 742411

print("El auto es {} y su matricula es {}".format(color,matricula)) #Forma antigua de formatear

print(f"El auto es {color} y su matricula es {matricula}") #forma actual para formatear partir de pytho 3.8