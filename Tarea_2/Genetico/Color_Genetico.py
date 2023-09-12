import random
import datetime

def leer_grafo_desde_archivo(nombre_archivo):
    grafo = {}
    with open(nombre_archivo, 'r') as file:
        lines = file.readlines()

    num_vertices, _ = map(int, lines[0].strip().split())

    for linea in lines[1:]:
        u, v = map(int, linea.strip().split())
        if u not in grafo:
            grafo[u] = []
        if v not in grafo:
            grafo[v] = []
        grafo[u].append(v)
        grafo[v].append(u)

    return grafo

def inicializar_poblacion(tamano_poblacion, nodos):
    poblacion = []
    for _ in range(tamano_poblacion):
        coloreado = {nodo: random.randint(0, len(nodos) - 1) for nodo in nodos}
        poblacion.append(coloreado)
    return poblacion

def calcular_costo_coloreado(coloreado, grafo):
    costo = 0
    for nodo, vecinos in grafo.items():
        for vecino in vecinos:
            if coloreado[nodo] == coloreado[vecino]:
                costo += 1
    return costo // 2  # Dividimos por 2 para contar cada arista una vez

def mutar_coloreado(coloreado, probabilidad_mutacion, nodos):
    mutado = coloreado.copy()
    for nodo in nodos:
        if random.random() < probabilidad_mutacion:
            mutado[nodo] = random.randint(0, len(nodos) - 1)
    return mutado

def cruzar_coloreados(padre1, padre2, nodos):
    punto_cruce = random.randint(1, len(nodos) - 1)
    hijo1 = {nodo: padre1[nodo] if i <= punto_cruce else padre2[nodo] for i, nodo in enumerate(nodos)}
    hijo2 = {nodo: padre2[nodo] if i <= punto_cruce else padre1[nodo] for i, nodo in enumerate(nodos)}
    return hijo1, hijo2

def seleccion_torneo(poblacion, grafo, k=2):
    seleccionados = []
    while len(seleccionados) < len(poblacion):
        participantes = random.sample(poblacion, k)
        mejor_participante = min(participantes, key=lambda x: calcular_costo_coloreado(x, grafo))
        seleccionados.append(mejor_participante)
    return seleccionados

def coloreador_genetico(nombre_archivo, tamano_poblacion, num_generaciones, probabilidad_mutacion):
    grafo = leer_grafo_desde_archivo(nombre_archivo)
    nodos = list(grafo.keys())
    mejor_coloreado = None
    mejor_costo = float('inf')

    poblacion = inicializar_poblacion(tamano_poblacion, nodos)

    for i in range(num_generaciones):
        poblacion = seleccion_torneo(poblacion, grafo)
        nuevos_coloreados = []
        
        for _ in range(tamano_poblacion // 2):
            padre1, padre2 = random.sample(poblacion, 2)
            hijo1, hijo2 = cruzar_coloreados(padre1, padre2, nodos)
            nuevos_coloreados.extend([mutar_coloreado(hijo1, probabilidad_mutacion, nodos), mutar_coloreado(hijo2, probabilidad_mutacion, nodos)])
        
        poblacion = nuevos_coloreados

        mejor_individuo = min(poblacion, key=lambda x: calcular_costo_coloreado(x, grafo))
        costo_mejor_individuo = calcular_costo_coloreado(mejor_individuo, grafo)

        if costo_mejor_individuo < mejor_costo:
            mejor_coloreado = mejor_individuo.copy()
            mejor_costo = costo_mejor_individuo

    num_colores = max(mejor_coloreado.values()) + 1  # Número de colores utilizados
    return num_colores, mejor_coloreado

if __name__ == '__main__':
    nombre_archivo = "gc_1000_9"
    tamano_poblacion = 100
    num_generaciones = 1000
    probabilidad_mutacion = 0.2
    start = datetime.datetime.now()
    num_colores, mejor_coloreado = coloreador_genetico(nombre_archivo, tamano_poblacion, num_generaciones, probabilidad_mutacion)
    end = datetime.datetime.now()
    print(f'Total: {end - start}')
    print(f"Número de colores utilizados: {num_colores}")
    for nodo, color in mejor_coloreado.items():
        print(f"Vértice {nodo}: Color {color}")
