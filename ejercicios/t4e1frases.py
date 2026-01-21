#Pedir al usuario que introduzca una frase
frase = input("Introduce una frase: ")

#Obtenemos la longitud de la frase
longitud = len(frase)

#Obtenemos la frase en mayuscula
frasemayusculas = frase.upper()

#Obtenemos la frase en minuscula
fraseminusculas = frase.lower()

print ("Imprimir la frase del usuario")
print ("Longitud", longitud)
print (frasemayusculas)
print (fraseminusculas)
