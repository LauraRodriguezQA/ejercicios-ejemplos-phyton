#Funcion para pedir color al usuario

def mensaje_color(color):
    mensaje = ""

    if color == "Rojo":
     mensaje = "El rojo es el color de la pasión y la energía. ¡Hoy será un día lleno de acción y emoción! No temas a los desafíos, saldrás victorioso."
    elif color == "Verde":
     mensaje = "El verde representa la esperanza y el crecimiento. Algo nuevo y positivo está por florecer en tu vida. Confía en los pequeños cambios que te acercan a tus metas."
    elif color == "Azul":
     mensaje = "El azul simboliza la calma y la serenidad. Hoy estarás rodeado de tranquilidad y equilibrio. Aprovecha este momento para reflexionar y renovar tu energía."
    elif color == "Amarillo":
     mensaje = "El amarillo es el color de la felicidad y el optimismo. ¡Prepárate para un día lleno de alegría y buenas noticias! Alguien cercano te sorprenderá de forma positiva."
    elif color == "Morado":
     mensaje = "El morado evoca la sabiduría y la creatividad. Hoy te sentirás inspiradoy lleno de ideas. Es el momento ideal para dejar volar tu imaginación y tomar decisiones importantes"
    else:
     mensaje = "Color no reconocido. Por favor elige uno de los siguientes colores: Rojo, Verde, Azul, Amarillo o Morado."

    return mensaje

#Pedimos al usuario que elija el color, funcion principal
def colorfavorito():

 color = (input("Elige tu color favorito (Rojo, Verde, Azul, Amarillo, Morado): "))
 mensaje = mensaje_color(color)
 print(mensaje_color(color))

#Funcion principal
colorfavorito()

