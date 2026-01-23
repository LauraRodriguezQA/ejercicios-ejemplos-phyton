def calcular_nota_media ():

numero_notas= int(input("Cuantas notas desea introducir?"))
#Repetimos el nimero de veces que ha indicado

for i in range(numero_notas):
    nota= float(input("Introduce la nota"))

#Sumamos al total 
suma += nota

#Calculamos la media, que es igual a la suma total, entre el numero de notas introducida
nota_media = suma/numero_notas

print("Nota media es: ", nota_media)

calcular_nota_media()