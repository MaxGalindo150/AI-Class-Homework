import random
import math
import datetime


start = datetime.datetime.now()
def calcular_conflictos(tablero):
    n = len(tablero)
    conflictos = 0
    for i in range(n):
        for j in range(i+1, n):
            if tablero[i] == tablero[j] or abs(tablero[i] - tablero[j]) == j - i:
                conflictos += 1
    return conflictos

def imprimir_tablero(tablero):
    n = len(tablero)
    for i in range(n):
        row = ""
        for j in range(n):
            if tablero[i] == j:
                row += "Q "
            else:
                row += ". "
        print(row)
    print()

def inicializar_tablero(N):
    tablero = list(range(N))
    random.shuffle(tablero)
    return tablero

def recocido_simulado(N, max_iteraciones, temperatura_inicial, enfriamiento):
    tablero_actual = inicializar_tablero(N)
    conflictos_actual = calcular_conflictos(tablero_actual)
    temperatura = temperatura_inicial
    mejor_tablero = tablero_actual
    mejor_conflictos = conflictos_actual

    for iteracion in range(max_iteraciones):
        if conflictos_actual == 0:
            return tablero_actual

        i, j = random.sample(range(N), 2)
        tablero_vecino = list(tablero_actual)
        tablero_vecino[i], tablero_vecino[j] = tablero_vecino[j], tablero_vecino[i]
        conflictos_vecino = calcular_conflictos(tablero_vecino)

        delta = conflictos_vecino - conflictos_actual

        if delta < 0 or random.random() < math.exp(-delta / temperatura):
            tablero_actual = tablero_vecino
            conflictos_actual = conflictos_vecino

        if conflictos_actual < mejor_conflictos:
            mejor_tablero = tablero_actual
            mejor_conflictos = conflictos_actual

        temperatura *= enfriamiento

    return mejor_tablero

N = 100
max_iteraciones = 100000
temperatura_inicial = 1.0
enfriamiento = 0.99

solucion = recocido_simulado(N, max_iteraciones, temperatura_inicial, enfriamiento)

end = datetime.datetime.now()

total_time = end - start


if solucion:
    print(f'Tiempo: {total_time} seg')
    print("Solución encontrada:")
    print(solucion)
    #imprimir_tablero(solucion)
else:
    print("No se encontró una solución en el número máximo de iteraciones.")
