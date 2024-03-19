import random

def generar_matriz_aleatoria(dim=3):
    """Genera una matriz cuadrada de 3x3 con números enteros aleatorios."""
    return [[random.randint(1, 100) for _ in range(dim)] for _ in range(dim)]

def determinanteSarrus(matriz):
    suma = 0
    suma += matriz[0][0] * matriz[1][1] * matriz[2][2]
    suma += matriz[0][1] * matriz[1][2] * matriz[2][0]
    suma += matriz[0][2] * matriz[1][0] * matriz[2][1]
    
    suma -= matriz[0][2] * matriz[1][1] * matriz[2][0]
    suma -=matriz[0][0] * matriz[1][2] * matriz[2][1]
    suma -=matriz[0][1] * matriz[1][0] * matriz[2][2]
    
    return suma

# Generar y calcular el determinante de una matriz 3x3 aleatoria
matriz_aleatoria = generar_matriz_aleatoria()
print("Matriz Aleatoria:", matriz_aleatoria)
print("Determinante (método iterativo):", determinanteSarrus(matriz_aleatoria))
