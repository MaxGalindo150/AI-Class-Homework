import datetime
def is_safe(grafo, v, c, color_actual):
    for i in range(len(grafo)):
        if grafo[v][i] == 1 and color_actual[i] == c:
            return False
    return True

def colorear_grafo(grafo, m, v, color_actual, num_colores):
    if v == len(grafo):
        return True
    
    for c in range(1, m + 1):
        if is_safe(grafo, v, c, color_actual):
            color_actual[v] = c
            if colorear_grafo(grafo, m, v + 1, color_actual, num_colores):
                return True
            color_actual[v] = 0
    
    return False

def resolver_coloreado_grafo(grafo):
    num_vertices = len(grafo)
    num_colores = 50  # Puedes ajustar el número de colores según tus necesidades
    color_actual = [0] * num_vertices
    
    if not colorear_grafo(grafo, num_colores, 0, color_actual, num_colores):
        return "No se pudo encontrar una solución"
    
    colores_utilizados = len(set(color_actual))
    solucion = [colores_utilizados] + color_actual
    
    return solucion

# Datos del grafo

with open('gc_1000_9', 'r') as file:
        lines = file.readlines()
num_vertices, num_edges = map(int, lines[0].split())
edges = [tuple(map(int, line.split())) for line in lines[1:]]

n = 1000

# Inicializar la matriz de adyacencia
grafo = [[0] * n for _ in range(n)]
for u, v in edges:
    grafo[u][v] = grafo[v][u] = 1

# Resolver el problema de coloreado de grafos
start = datetime.datetime.now()
solucion = resolver_coloreado_grafo(grafo)
end = datetime.datetime.now()
# Imprimir la solución
if type(solucion) == str:
    print(f'Timepo: {end-start}')
    print(solucion)
else:
    print(f'Timepo: {end-start}')
    print("Número de colores utilizados:", solucion[0])
    for i in range(n):
        print(f"Vértice {i}: Color {solucion[i + 1]}")
