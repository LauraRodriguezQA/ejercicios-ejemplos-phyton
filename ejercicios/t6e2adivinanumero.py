#Funcion para establecer el numero ganador
def adivinar_numero(numero):
    numero_ganador = 4 #numero ganador
    mensaje = ""

#Asignar el mensaje

    if numero == numero_ganador:
     mensaje = "¡Haz ganado! El numero es el correcto."
    else:
       mensaje = f"Lo siento, perdiste. El numero correcto era el {numero_ganador}"
       
       return mensaje 
    
    #Funcion principal
def adivinanza_numero():
   
   #Pedir al usuario que intruzca un numero del 1 al 10 
   
 numero_usuario = int(input("Introducir un numero del 1 al 10: "))

#Mostrar el mensaje segun el numero elegido
 mensaje = adivinar_numero(numero_usuario)
 print (mensaje)

#Llamada funcion principal 
adivinanza_numero()

