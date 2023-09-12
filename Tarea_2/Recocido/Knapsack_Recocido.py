import random
import math
import datetime

# Definir la función de evaluación (en este caso, maximizar el valor total)
def eval_solution(solution, values, weights, max_weight):
    total_value = sum(value * solution[i] for i, value in enumerate(values))
    total_weight = sum(weight * solution[i] for i, weight in enumerate(weights))
    if total_weight > max_weight:
        return -1  # Penalizar soluciones que excedan la capacidad
    return total_value

# Implementación del algoritmo de recocido simulado
def simulated_annealing(values, weights, max_weight, initial_temp, cooling_rate, num_iterations):
    num_items = len(values)
    current_solution = [random.randint(0, 1) for _ in range(num_items)]
    current_value = eval_solution(current_solution, values, weights, max_weight)
    
    best_solution = current_solution.copy()
    best_value = current_value
    
    start_time = datetime.datetime.now()  # Iniciar el contador de tiempo
    
    for iteration in range(num_iterations):
        temperature = initial_temp / (1 + iteration)
        
        # Generar una solución vecina
        neighbor_solution = current_solution.copy()
        random_index = random.randint(0, num_items - 1)
        neighbor_solution[random_index] = 1 - neighbor_solution[random_index]
        
        neighbor_value = eval_solution(neighbor_solution, values, weights, max_weight)
        
        # Calcular la diferencia en la función de evaluación
        delta_value = neighbor_value - current_value
        
        # Si la solución vecina es mejor o se acepta según la probabilidad, actualizar
        if delta_value > 0 or random.random() < math.exp(delta_value / temperature):
            current_solution = neighbor_solution
            current_value = neighbor_value
            
            if current_value > best_value:
                best_solution = current_solution.copy()
                best_value = current_value
    
    end_time = datetime.datetime.now()  # Finalizar el contador de tiempo
    execution_time = end_time - start_time  # Calcular el tiempo de ejecución
    
    return best_solution, best_value, execution_time

if __name__ == "__main__":
    with open('../Tarea_1/ks_19_0', 'r') as file:
        first_line = file.readline().split()
        num_elements = int(first_line[0])
        capacity = int(first_line[1])
       
        weights = []
        values = []
        
        for _ in range(num_elements):
            v, w = map(int, file.readline().split())
            weights.append(w)
            values.append(v)
    
    initial_temp = 100.0
    cooling_rate = 0.01
    num_iterations = 10100

    # Obtener la mejor solución, su valor y tiempo de ejecución
    best_solution, best_value, execution_time = simulated_annealing(values, weights, capacity, initial_temp, cooling_rate, num_iterations)

    # Imprimir la capacidad, el peso en la mochila, el valor en la mochila y el tiempo de ejecución
    print(f"Tiempo: {execution_time}")
    print(f"Capacidad de la mochila: {capacity}")
    print(f"Peso en la mochila: {sum(weights[i] * best_solution[i] for i in range(len(best_solution)))}")
    print(f"Valor en la mochila: {best_value}")
    print(f"Elementos seleccionados en la mochila: {best_solution}")
    