import turtle

# Configuración de colores para cada número (0-9)
colores = {
    0: "white",    # Fondo
    1: "red",
    2: "blue",
    3: "green",
    4: "yellow",
    5: "purple",
    6: "orange",
    7: "pink",
    8: "brown",
    9: "cyan"
}

def crear_archivo(): #Crea un archivo de ejemplo con números del 0-9 en una matriz 100x100
    import random
    
    # Crear una matriz con variedad de colores
    with open("matriz_colores.txt", "w") as archivo:
        for i in range(100):
            fila = []
            for j in range(100):
                # Crear patrones interesantes para visualización
                if i < 10:  # Primera fila: números ordenados
                    numero = j % 10
                elif i < 20:  # Segunda fila: gradiente
                    numero = (j // 10) % 10
                elif 40 <= i < 60 and 40 <= j < 60:  # Cuadrado central
                    numero = random.randint(1, 9)
                elif i == j or i + j == 99:  # Diagonales
                    numero = random.choice([1, 2, 3])
                else:  # Patrón aleatorio con distribución variada
                    numero = random.choices(
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        weights=[30, 10, 10, 10, 10, 5, 5, 5, 5, 10]
                    )[0]
                fila.append(str(numero))
            archivo.write("".join(fila) + "\n")

def leer_matriz(nombre_archivo): #Lee la matriz desde el archivo
    matriz = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            fila = [int(caracter) for caracter in linea.strip()]
            matriz.append(fila)
    return matriz

def dibujar_matriz_turtle(matriz, colores): #Dibuja la matriz usando Turtle
    # Configurar la ventana
    pantalla = turtle.Screen()
    pantalla.setup(800, 800)
    pantalla.title("Matriz de Colores 100x100")
    pantalla.tracer(0)  # Desactivar animación para mayor velocidad
    
    # Configurar turtle
    artista = turtle.Turtle()
    artista.speed(0)
    artista.penup()
    artista.hideturtle()
    
    # Tamaño de cada píxel
    tamano_pixel = 8
    desplazamiento = tamano_pixel * 100 / 2
    
    # Dibujar cada píxel
    for y in range(100):
        for x in range(100):
            numero = matriz[y][x]
            color = colores[numero]
            
            # Calcular posición
            pos_x = x * tamano_pixel - desplazamiento
            pos_y = desplazamiento - y * tamano_pixel
            
            # Dibujar el píxel
            artista.goto(pos_x, pos_y)
            artista.dot(tamano_pixel, color)
    
    pantalla.update()
    pantalla.exitonclick()

# Programa principal
def main():
    # Crear archivo de ejemplo si no existe
    try:
        matriz = leer_matriz("matriz_colores.txt")
    except FileNotFoundError:
        print("Creando archivo...")
        crear_archivo()
        matriz = leer_matriz("matriz_colores.txt")
    
    print("Matriz cargada correctamente")
    print(f"Tamano: {len(matriz)}x{len(matriz[0])}")
    
    # Mostrar estadísticas de colores
    conteo_colores = {num: 0 for num in range(10)}
    for fila in matriz:
        for numero in fila:
            conteo_colores[numero] += 1
    
    print("\nDistribucion de colores:")
    for num, color in colores.items():
        print(f"Numero {num} ({color}): {conteo_colores[num]} pixeles")
    
    # Dibujar con Turtle
    print("\nDibujando matriz... Haz click para cerrar.")
    dibujar_matriz_turtle(matriz, colores)

if __name__ == "__main__":
    main()