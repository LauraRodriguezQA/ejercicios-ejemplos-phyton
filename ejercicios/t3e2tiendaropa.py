#Precios
precio_camiseta = 10.0
precio_sudadera = 20.5
precio_gorra = 5.5
iva = 0.21  #IVA del 21%

#Pedir cantidades al usuario
cantidad_camisetas = int(input("Introduce la cantidad de camisetas: "))
cantidad_sudaderas = int(input("Introduce la cantidad de sudaderas: "))
cantidad_gorras = int(input("Introduce la cantidad de gorras: "))

#Subtotal de la compra
subtotal = (cantidad_camisetas * precio_camiseta +
            cantidad_sudaderas * precio_sudadera +
            cantidad_gorras * precio_gorra)

#Total con IVA
subtotal = subtotal * iva
total_compra = subtotal + iva

#Mostrar el total de la compra
print("\nResumen de la compra: ")
print("Subtotal: ", subtotal, "euros")
print("IVA (21%):", iva, "euros")
print("Total con IVA:", total_compra, "euros")








