#Datos cancion favorita
print ("Introduce los datos de tu cancion favorita")
titulo = input("Título de la canción: ")
artista = input("Artista: ")
album = input ("Album: ")
año = int(input("Año de lanzamiento: "))
duracion = int(input("Duracion en segundos: "))
tiene_videoclip = input("¿Tiene videoclip? (True/False): ").capitalize() == "True"

#Imprimir variables
print("\nDatos de tu canción favorita:")
print ("titulo", titulo)
print ("artista", artista)
print ("album", album)
print ("año lanzamiento",año)
print ("duracion en segundos", duracion)
print ("tiene videoclip?", tiene_videoclip)


# Datos de la canción menos favorita ingresados por el usuario
print("\nIntroduce los datos de la canción que menos te gusta:")
titulo = input("Título de la canción: ")
artista = input("Artista: ")
album = input("Álbum: ")
año = int(input("Año de lanzamiento: "))
duracion = int(input("Duración (en segundos): "))
tiene_videoclip = input("¿Tiene videoclip? (True/False): ").capitalize() == "True"

# Mostrar datos de la canción menos favorita
print("\nDatos de la canción que menos te gusta:")
print("Título:", titulo)
print("Artista:", artista)
print("Álbum:", album)
print("Año de lanzamiento:", año)
print("Duración (segundos):", duracion)
print("¿Tiene videoclip?:", tiene_videoclip)


