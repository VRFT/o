import random
from PIL import Image #Biblioteca para manejar imagenes 
import os #manejo de operaciones del so

frutas = ["zarzamora", "uva", "sandia", "platano", "pera", "papaya", "manzana", "mango", "mandarina", "fresa", "ciruela"]

# Ordenar aleatoriamente la lista de frutas
ordenar = random.sample(frutas, len(frutas))

# Aqui alojamos las imagenes a utilizar
imagenes = r"C:\Users\vecto\OneDrive\Escritorio\Practica\imagenes_frutas"

# Se iteran las imagenes y se muestran 
for fruta in ordenar:
    print(f"Fruta: {fruta}")

    # Construir la imagen concatenando el directorio de la imagen 
    ruta_imagen = os.path.join(imagenes, f"{fruta.lower()}.jpg")
    print(f"Ruta de la imagen: {ruta_imagen}")

    try:
        # Se carga la imagen utilizando PIL, si esta no se encuentra se maneja la excepción
        imagen = Image.open(ruta_imagen)
        imagen.show()
        print("Imagen mostrada")
    except FileNotFoundError:
        print(f"No se encontró la imagen para {fruta}")

   #  imprime una línea de guiones para separar las salidas de cada fruta.
    print("-" * 30)