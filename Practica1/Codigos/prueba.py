import pygame

# Inicializar Pygame
pygame.init()

# Definir las dimensiones de la pantalla y la cuadrícula
ancho_pantalla = 800
alto_pantalla = 600
tamano_celda = 40
filas = alto_pantalla // tamano_celda
columnas = ancho_pantalla // tamano_celda

# Colores
NEGRO = (0, 0, 0)
GRIS = (128, 128, 128)

# Crear la pantalla
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Cuadrícula en Pygame")

def dibujar_cuadricula():
    for fila in range(filas):
        for columna in range(columnas):
            rect = pygame.Rect(columna * tamano_celda, fila * tamano_celda, tamano_celda, tamano_celda)
            pygame.draw.rect(pantalla, NEGRO, rect, 1)  # El 1 dibuja solo el borde del rectángulo

# Bucle principal del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Rellenar la pantalla de gris
    pantalla.fill(GRIS)

    # Dibujar la cuadrícula
    dibujar_cuadricula()

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
