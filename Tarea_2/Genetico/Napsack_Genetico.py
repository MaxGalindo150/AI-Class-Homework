import random
import datetime
def leer_datos_desde_archivo(nombre_archivo):
    # Lee los datos del archivo de la mochila
    with open(nombre_archivo, 'r') as file:
        lines = file.readlines()

    num_elementos, capacidad_mochila = map(int, lines[0].strip().split())
    elementos = []

    for linea in lines[1:]:
        valor, peso = map(int, linea.strip().split())
        elementos.append((valor, peso))

    return num_elementos, capacidad_mochila, elementos

def inicializar_poblacion(tamano_poblacion, num_elementos):
    # Inicializa la población con soluciones aleatorias
    poblacion = []
    for _ in range(tamano_poblacion):
        solucion = [random.randint(0, 1) for _ in range(num_elementos)]
        poblacion.append(solucion)
import random

def leer_datos_desde_archivo(nombre_archivo):
    # Lee los datos del archivo de la mochila
    with open(nombre_archivo, 'r') as file:
        lines = file.readlines()

    num_elementos, capacidad_mochila = map(int, lines[0].strip().split())
    elementos = []

    for linea in lines[1:]:
        valor, peso = map(int, linea.strip().split())
        elementos.append((valor, peso))

    return num_elementos, capacidad_mochila, elementos

def inicializar_poblacion(tamano_poblacion, num_elementos):
    # Inicializa la población con soluciones aleatorias
    poblacion = []
    for _ in range(tamano_poblacion):
        solucion = [random.randint(0, 1) for _ in range(num_elementos)]
        poblacion.append(solucion)
    return poblacion

def evaluar_solucion(solucion, elementos, capacidad_mochila):
    # Evalúa una solución calculando el valor total y el peso total en la mochila
    valor_total = 0
    peso_total = 0
    for i in range(len(solucion)):
        if solucion[i] == 1:
            valor, peso = elementos[i]
            valor_total += valor
            peso_total += peso
    if peso_total <= capacidad_mochila:
        return valor_total, peso_total
    else:
        return 0, peso_total

def mutar_solucion(solucion, probabilidad_mutacion):
    # Realiza una mutación en la solución (cambia aleatoriamente un elemento)
    mutado = solucion.copy()
    for i in range(len(mutado)):
        if random.random() < probabilidad_mutacion:
            mutado[i] = 1 - mutado[i]  # Cambia 0 a 1 o 1 a 0
    return mutado

def seleccionar_mejores_padres(poblacion, elementos, capacidad_mochila):
    # Selecciona los dos mejores padres basados en su valor total
    poblacion_ordenada = sorted(poblacion, key=lambda solucion: -evaluar_solucion(solucion, elementos, capacidad_mochila)[0])
    return poblacion_ordenada[0], poblacion_ordenada[1]

def cruzar_soluciones(padre1, padre2):
    # Realiza el cruce de dos soluciones para generar dos hijos
    punto_cruce = random.randint(1, len(padre1) - 1)
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
    hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
    return hijo1, hijo2

def mochila_genetico(nombre_archivo, tamano_poblacion, num_generaciones, probabilidad_mutacion):
    num_elementos, capacidad_mochila, elementos = leer_datos_desde_archivo(nombre_archivo)
    mejor_solucion = None
    mejor_valor = 0

    poblacion = inicializar_poblacion(tamano_poblacion, num_elementos)

    for i in range(num_generaciones):
        for j in range(tamano_poblacion):
            solucion_actual = poblacion[j]
            valor_actual, peso_actual = evaluar_solucion(solucion_actual, elementos, capacidad_mochila)
            vecino = mutar_solucion(solucion_actual, probabilidad_mutacion)
            valor_vecino, peso_vecino = evaluar_solucion(vecino, elementos, capacidad_mochila)

            if valor_vecino > valor_actual:
                poblacion[j] = vecino
                valor_actual = valor_vecino
                peso_actual = peso_vecino

        padre1, padre2 = seleccionar_mejores_padres(poblacion, elementos, capacidad_mochila)
        hijo1, hijo2 = cruzar_soluciones(padre1, padre2)
        poblacion.extend([hijo1, hijo2])

        poblacion = poblacion[:tamano_poblacion]

        valor_mejor_actual, peso_mejor_actual = evaluar_solucion(poblacion[0], elementos, capacidad_mochila)
        if valor_mejor_actual > mejor_valor:
            mejor_valor = valor_mejor_actual
            mejor_solucion = poblacion[0]

    return mejor_valor, mejor_solucion, capacidad_mochila, evaluar_solucion(mejor_solucion, elementos, capacidad_mochila)[1]

if __name__ == '__main__':
    nombre_archivo = "../Tarea_1/ks_19_0"
    tamano_poblacion = 100
    num_generaciones = 1000
    probabilidad_mutacion = 0.2
    start = datetime.datetime.now()
    mejor_valor, mejor_solucion, capacidad_mochila, peso_en_mochila = mochila_genetico(nombre_archivo, tamano_poblacion, num_generaciones, probabilidad_mutacion)
    end = datetime.datetime.now()

    print(f"Tiempo: {end-start}")
    print(f"Capacidad de la mochila: {capacidad_mochila}")
    print(f"Peso en la mochila: {peso_en_mochila}")
    print(f"Mejor valor encontrado: {mejor_valor}")
    print(f"Mejor solución: {mejor_solucion}")

