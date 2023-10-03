import numpy as np
import random

# Función eggholder
def eggholder(x, y):
    term1 = -(y + 47) * np.sin(np.sqrt(np.abs(x / 2 + (y + 47))))
    term2 = -x * np.sin(np.sqrt(np.abs(x - (y + 47))))
    return term1 + term2

# Crear población inicial
def crear_poblacion(n_ind, lim_inf, lim_sup):
    return np.random.uniform(lim_inf, lim_sup, size=(n_ind, 2))

# Calcular el valor de adaptación para toda la población (buscamos el mínimo)
def calcular_valor_adaptacion(poblacion):
    return eggholder(poblacion[:, 0], poblacion[:, 1])

# Selección de padres basada en torneo
def seleccionar_padres(poblacion, valores_adaptacion, num_padres):
    indices = np.random.choice(len(poblacion), (num_padres, 2))
    indices_padres = np.where(valores_adaptacion[indices[:, 0]] < valores_adaptacion[indices[:, 1]], indices[:, 0], indices[:, 1])
    return poblacion[indices_padres]

# Cruce de los padres para generar descendencia
def cruzar(padres, num_descendencia):
    descendencia = padres[np.random.choice(len(padres), num_descendencia, replace=True)]
    puntos_cruce = np.random.randint(2, size=(num_descendencia, 2), dtype=bool)
    descendencia[puntos_cruce] = descendencia[puntos_cruce[::-1]]
    return descendencia

# Mutación de los hijos
def mutar(descendencia, tasa_mutacion, escala_mutacion):
    mascara = np.random.random(descendencia.shape) < tasa_mutacion
    mutacion = np.random.normal(scale=escala_mutacion, size=descendencia.shape)
    descendencia += mascara * mutacion
    return descendencia

# Algoritmo genético principal
def algoritmo_genetico(num_generaciones, tamano_poblacion, tasa_mutacion, escala_mutacion):
    limite_inferior = -512
    limite_superior = 512
    num_padres = tamano_poblacion // 2
    num_descendencia = tamano_poblacion - num_padres

    # Crear población inicial
    poblacion = crear_poblacion(tamano_poblacion, limite_inferior, limite_superior)
    
    for generacion in range(num_generaciones):
        # Calcular el valor de adaptación para la población actual
        valores_adaptacion = calcular_valor_adaptacion(poblacion)

        # Seleccionar padres
        padres = seleccionar_padres(poblacion, valores_adaptacion, num_padres)

        # Cruzar los padres para generar descendencia
        descendencia = cruzar(padres, num_descendencia)

        # Aplicar mutación a la descendencia
        descendencia = mutar(descendencia, tasa_mutacion, escala_mutacion)

        # Reemplazar la población actual por la descendencia
        poblacion[:num_padres] = padres
        poblacion[num_padres:] = descendencia

        # Encontrar el mejor individuo de esta generación
        mejor_valor_adaptacion = min(valores_adaptacion)
        mejor_individuo = poblacion[np.argmin(valores_adaptacion)]

        # Imprimir información de la generación actual
        print(f"Generación {generacion + 1}: Mejor valor de adaptación = {mejor_valor_adaptacion:.4f}, Mejor individuo = {mejor_individuo}")

    return mejor_individuo, mejor_valor_adaptacion

if __name__ == "__main__":
    num_generaciones = 100
    tamano_poblacion = 100
    tasa_mutacion = 0.1
    escala_mutacion = 10.0

    mejor_solucion, mejor_valor_adaptacion = algoritmo_genetico(num_generaciones, tamano_poblacion, tasa_mutacion, escala_mutacion)

    print("\nMejor solución encontrada:")
    print(f"Coordenadas (x, y): {mejor_solucion}")
    print(f"Valor de la función eggholder: {mejor_valor_adaptacion:.4f}")
