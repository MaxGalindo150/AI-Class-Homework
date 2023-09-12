import random
import math
import datetime

def algoritmo_genetico_eggholder(tamano_poblacion, num_generaciones, probabilidad_mutacion):
    def inicializar_poblacion():
        # Inicializa la población con soluciones aleatorias en el rango [-512, 512]
        poblacion = []
        for _ in range(tamano_poblacion):
            solucion = [random.uniform(-512, 512), random.uniform(-512, 512)]
            poblacion.append(solucion)
        return poblacion

    def calcular_valor_solucion(solucion):
        # Calcula el valor de la función Eggholder para una solución
        x, y = solucion
        value = -(y + 47) * math.sin(math.sqrt(abs(x/2 + y + 47))) - x * math.sin(math.sqrt(abs(x - (y + 47))))
        return value

    def mutar_solucion(solucion):
        # Realiza una mutación en la solución (cambia aleatoriamente un componente)
        mutado = solucion.copy()
        for i in range(len(mutado)):
            if random.random() < probabilidad_mutacion:
                mutado[i] = random.uniform(-512, 512)
        return mutado

    poblacion = inicializar_poblacion()
    mejor_solucion = None
    mejor_valor = float('inf')  # Cambio a 'inf' para minimización

    for generacion in range(num_generaciones):
        for i in range(tamano_poblacion):
            solucion_actual = poblacion[i]
            valor_actual = calcular_valor_solucion(solucion_actual)

            # Mutación
            if random.random() < probabilidad_mutacion:
                vecino = mutar_solucion(solucion_actual)
                valor_vecino = calcular_valor_solucion(vecino)

                # Aceptamos el vecino si es mejor que la solución actual
                if valor_vecino < valor_actual:  # Cambio a '<' para minimización
                    poblacion[i] = vecino

        # Actualizamos la mejor solución
        mejor_solucion_actual = min(poblacion, key=calcular_valor_solucion)  # Cambio a 'min' para minimización
        mejor_valor_actual = calcular_valor_solucion(mejor_solucion_actual)

        if mejor_valor_actual < mejor_valor:  # Cambio a '<' para minimización
            mejor_valor = mejor_valor_actual
            mejor_solucion = mejor_solucion_actual.copy()

    return mejor_valor, mejor_solucion

if __name__ == '__main__':
    tamano_pob = 100
    num_generaciones = 1000
    probabilidad_mutacion = 0.1
    start = datetime.datetime.now()
    mejor_valor, mejor_solucion = algoritmo_genetico_eggholder(tamano_pob, num_generaciones, probabilidad_mutacion)
    end = datetime.datetime.now()
    print(f'Tiempo: {end - start}')
    print(f"Mejor valor en Eggholder: {mejor_valor}")
    print(f"Mejor solución (x, y): {mejor_solucion}")
