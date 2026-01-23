def calcular_nota_media():
    #Pedimos cuántas notas va a introducir
    numero_notas = int(input("¿Cuántas notas desea introducir? "))

    #Inicializamos la suma
    suma = 0

    #Pedimos cada nota y la sumamos
    for i in range(numero_notas):
        nota = float(input("Introduce la nota: "))
        suma += nota

    #Calculamos la media
    nota_media = suma / numero_notas

    #Mostramos el resultado
    print("La nota media es:", nota_media)


#Ejecutamos la función
calcular_nota_media()