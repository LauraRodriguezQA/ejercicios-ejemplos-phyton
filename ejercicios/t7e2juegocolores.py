def juego_colores():

    #Pedimos al usuario que introduzca 5 colores
    premio = False #Variable creada por si el usuario no introduce el color ganador.
    for i in range(5):
        color = input("Introduce un color: ")
            #Si el color es azul (gana premio) 
        if (color.upper() == "AZUL"):
            premio = True
    
    #Cuando termina de introducir los colores, si ha ganado el premio, se muestra el texto, sino se muestra que no ha ganado.
    if(premio):
        print("HA GANADO EL PREMIO")
    else:
        print("NO HA GANADO")

#Ejecutamos la funcion
juego_colores()