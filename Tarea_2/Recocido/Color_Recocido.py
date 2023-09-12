import random
import math
import datetime

def leer_grafo(archivo):
    grafo = {}
    lineas = archivo.readlines()
    num_vertices, num_aristas = map(int, lineas[0].split())
    
    for linea in lineas[1:]:
        v1, v2 = map(int, linea.split())
        grafo.setdefault(v1, []).append(v2)
        grafo.setdefault(v2, []).append(v1)
    
    return grafo, num_vertices

def colorear_grafo(grafo, num_colores, T_inicial, T_final, enfriamiento):
    # Función para verificar si un coloreo es válido
    def es_coloreo_valido(coloreo):
        for vertice, vecinos in grafo.items():
            for vecino in vecinos:
                if coloreo[vertice] == coloreo[vecino]:
                    return False
        return True
    
    # Inicialización aleatoria de los colores
    coloreo_actual = {vertice: random.randint(1, num_colores) for vertice in grafo}
    
    # Función de costo (número de conflictos)
    def costo(coloreo):
        conflictos = 0
        for vertice, vecinos in grafo.items():
            for vecino in vecinos:
                if coloreo[vertice] == coloreo[vecino]:
                    conflictos += 1
        return conflictos // 2  # Utiliza división entera para contar cada conflicto una sola vez
    
    costo_actual = costo(coloreo_actual)
    mejor_coloreo = coloreo_actual.copy()
    mejor_costo = costo_actual
    
    T = T_inicial
    
    while T > T_final:
        # Generar un nuevo coloreo al hacer una pequeña modificación
        vertice_modificado = random.choice(list(grafo.keys()))
        color_nuevo = random.randint(1, num_colores)
        coloreo_nuevo = coloreo_actual.copy()
        coloreo_nuevo[vertice_modificado] = color_nuevo
        
        delta_costo = costo(coloreo_nuevo) - costo_actual
        
        if delta_costo < 0 or random.random() < math.exp(-delta_costo / T):
            coloreo_actual = coloreo_nuevo
            costo_actual = costo(coloreo_actual)
            
            if costo_actual < mejor_costo:
                mejor_coloreo = coloreo_actual.copy()
                mejor_costo = costo_actual
        
        T *= enfriamiento
    
    return mejor_coloreo, mejor_costo

# Leer el grafo desde un archivo (sustituye 'nombre_archivo' por el nombre de tu archivo)
with open('gc_50_7', 'r') as archivo:
    grafo, num_vertices = leer_grafo(archivo)

n = 1000  # El número de colores disponibles
intial_temp = 100.0  # Temperatura inicial
final_temp = 0.01  # Temperatura final
cooling_rate = 0.99  # Factor de enfriamiento

# Resolver el problema de coloreado de grafos
start = datetime.datetime.now()
mejor_coloreo, mejor_costo = colorear_grafo(grafo, n, intial_temp, final_temp, cooling_rate)
end = datetime.datetime.now()
# Imprimir la salida
num_colores_utilizados = len(set(mejor_coloreo.values()))
print(f'Timepo: {end-start}')
print("Numero de colores utilizados: ", num_colores_utilizados)

for vertice, color in mejor_coloreo.items():
    print(f"Vertice: {vertice}, Color: {color}")
