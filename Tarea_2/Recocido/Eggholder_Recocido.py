import math
import random
import datetime

def egg_holder(x, y):
    return -(y + 47) * math.sin(math.sqrt(abs(x/2 + (y + 47)))) - x * math.sin(math.sqrt(abs(x - (y + 47))))

def generate_neighbor(solution, step_size=1.0):
    x, y = solution
    x_new = x + random.uniform(-step_size, step_size)
    y_new = y + random.uniform(-step_size, step_size)
    return (x_new, y_new)

def simulated_annealing(initial_solution, initial_temperature, cooling_rate, num_iterations):
    current_solution = initial_solution
    current_cost = egg_holder(*current_solution)
    best_solution = current_solution
    best_cost = current_cost
    
    for i in range(num_iterations):
        # Genera una solución vecina
        neighbor_solution = generate_neighbor(current_solution, step_size=5.0)
        neighbor_cost = egg_holder(*neighbor_solution)
        
        # Calcula la diferencia en costos
        cost_difference = neighbor_cost - current_cost
        
        # Si la nueva solución es mejor o se acepta con una cierta probabilidad
        if cost_difference < 0 or random.random() < math.exp(-cost_difference / initial_temperature):
            current_solution = neighbor_solution
            current_cost = neighbor_cost
            
            # Actualiza la mejor solución encontrada si es mejor
            if current_cost < best_cost:
                best_solution = current_solution
                best_cost = current_cost
        
        # Enfría la temperatura
        initial_temperature *= cooling_rate
    
    return best_solution, best_cost

# Parámetros
initial_solution = (random.uniform(-512, 512), random.uniform(-512, 512))
initial_temperature = 1000.0
cooling_rate = 0.995  # Ajusta el enfriamiento más lento para buscar el mínimo global
num_iterations = 100000  # Aumenta el número de iteraciones para mejorar la búsqueda

# Ejecuta el algoritmo
start = datetime.datetime.now()
best_solution, best_cost = simulated_annealing(initial_solution, initial_temperature, cooling_rate, num_iterations)
end = datetime.datetime.now()
print(f"Tiempo: {end - start}")
print(f"Mejor solución encontrada: {best_solution}")
print(f"Valor mínimo encontrado: {best_cost}")
