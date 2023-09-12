import random
import multiprocessing
import datetime

start = datetime.datetime.now()
def generar_tablero(n):
    # Genera un tablero de ajedrez de n x n con reinas en filas aleatorias
    tablero = [random.randint(0, n-1) for _ in range(n)]
    return tablero

def calcular_colisiones(tablero):
    # Calcula el número de colisiones entre reinas en el tablero
    n = len(tablero)
    colisiones = 0
    for i in range(n):
        for j in range(i+1, n):
            if tablero[i] == tablero[j] or abs(tablero[i] - tablero[j]) == abs(i - j):
                colisiones += 1
    return colisiones

def mutar_tablero(tablero):
    # Realiza una mutación en el tablero (mueve una reina)
    n = len(tablero)
    fila = random.randint(0, n-1)
    nueva_columna = random.randint(0, n-1)
    tablero[fila] = nueva_columna
    return tablero

def seleccionar_mejor_tablero(poblacion):
    # Selecciona el mejor tablero basado en el número de colisiones
    mejor_tablero = min(poblacion, key=calcular_colisiones)
    return mejor_tablero, calcular_colisiones(mejor_tablero)

def buscar_solucion_n_reinas(n, tamano_poblacion, num_generaciones, probabilidad_mutacion, num_procesos):
    poblacion = [generar_tablero(n) for _ in range(tamano_poblacion)]
    pool = multiprocessing.Pool(processes=num_procesos)

    for _ in range(num_generaciones):
        poblacion = pool.map(mutate_and_select, poblacion)
        mejor_tablero, mejor_colisiones = seleccionar_mejor_tablero(poblacion)

        if mejor_colisiones == 0:
            break

    pool.close()
    pool.join()

    return mejor_tablero, mejor_colisiones

def mutate_and_select(tablero):
    # Realiza una mutación en el tablero y selecciona el mejor entre el original y el mutado
    colisiones_original = calcular_colisiones(tablero)
    nuevo_tablero = mutar_tablero(tablero)
    colisiones_mutado = calcular_colisiones(nuevo_tablero)

    if colisiones_mutado < colisiones_original:
        return nuevo_tablero
    else:
        return tablero

if __name__ == '__main__':
    n = 8  # Número de reinas
    tamano_poblacion = 1000
    num_generaciones = 1000
    probabilidad_mutacion = 0.3
    num_procesos = multiprocessing.cpu_count()

    mejor_tablero, mejor_colisiones = buscar_solucion_n_reinas(n, tamano_poblacion, num_generaciones, probabilidad_mutacion, num_procesos)
    end = datetime.datetime.now()

    print(f"Tiempo: {end-start} seg")
    print(f"Número de reinas: {n}")
    print(f"Mejor tablero encontrado: {mejor_tablero}")
    print(f"Número de colisiones: {mejor_colisiones}")
