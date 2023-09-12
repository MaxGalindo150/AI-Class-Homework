import numpy as np
import datetime

def knapsack_backtracking(weights, values, capacity):
    n = len(weights)
    selected_items = [0] * n

    def backtrack(current_weight, current_value, index):
        if index == n or current_weight >= capacity:
            return current_value, current_weight

        if current_weight + weights[index] <= capacity:
            selected_items[index] = 1
            max_value_with, total_weight_with = backtrack(
                current_weight + weights[index],
                current_value + values[index],
                index + 1
            )
            selected_items[index] = 0
            max_value_without, total_weight_without = backtrack(
                current_weight, current_value, index + 1
            )

            if max_value_with > max_value_without:
                selected_items[index] = 1
                return max_value_with, total_weight_with
            else:
                selected_items[index] = 0
                return max_value_without, total_weight_without
        else:
            return backtrack(current_weight, current_value, index + 1)

    max_value, total_weight = backtrack(0, 0, 0)
    return max_value, total_weight, selected_items

def solve_knapsack(file_path):
    start = datetime.datetime.now()
    with open(file_path, 'r') as file:
        first_line = file.readline().split()
        num_elements = int(first_line[0])
        capacity = int(first_line[1])

        weights = []
        values = []

        for _ in range(num_elements):
            v, w = map(int, file.readline().split())
            weights.append(w)
            values.append(v)

    max_value, total_weight, selected_items = knapsack_backtracking(weights, values, capacity)
    end = datetime.datetime.now()

    print(f'Tiempo: {end-start}')
    print(f"Capacidad de la mochila: {capacity}")
    print(f"Peso total en la mochila: {total_weight}")
    print(f"Valor máximo en la mochila: {max_value}")
    
    # Devolver el array de elementos seleccionados (0 o 1)
    return selected_items

# Ejemplo de uso
file_path = '../Tarea_1/ks_19_0'
selected_items = solve_knapsack(file_path)
print("Elementos seleccionados en la mochila:", selected_items)
