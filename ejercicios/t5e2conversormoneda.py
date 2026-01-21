#Función para convertir euros a dólares
def convertir_a_dolares(euros):
    return euros * 1.1  

#Función para convertir euros a libras
def convertir_a_libras(euros):
    return euros * 0.87  

#Función principal para la conversión
def conversor_de_monedas():
    euros = float(input("Introduce la cantidad en euros: "))

    dolares = convertir_a_dolares(euros) 
    libras = convertir_a_libras(euros)    

    # Mostrar los resultados de forma clara
    print("Cantidad en euros:", euros)
    print("Equivalente en dólares:", dolares)
    print("Equivalente en libras:", libras)

# Llamar a la función principal
conversor_de_monedas()
