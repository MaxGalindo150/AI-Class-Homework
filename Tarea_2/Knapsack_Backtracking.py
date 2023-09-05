import numpy as np

with open('../Tarea_1/ks_19_0', 'r') as file:
       first_line = file.readline().split()
       num_elements = int(first_line[0])
       capacity = int(first_line[1])
       
       weights = []
       values = []
       v_w = []                             # Create tree with the items from ks_19_0
       for _ in range(num_elements):
           v, w = map(int, file.readline().split())
           weights.append(w)
           values.append(v)
           v_w.append(v/w)

print(np.mean(v_w))


class Knapsack:
    def __init__(self, weights, values, capacity):
        self.weights = weights  # Lista de pesos de los elementos
        self.values = values    # Lista de valores de los elementos
        self.capacity = capacity  # Capacidad máxima de la mochila
        self.n = len(weights)   # Número de elementos
        self.selected_items = [0] * self.n
    def knapsack_backtracking(self, current_weight, current_value, index):
        if index == self.n or current_weight >= self.capacity:
            return current_value, current_weight  # Detiene la recursión si se alcanza la capacidad o se agotan los elementos
        if current_weight + self.weights[index] <= self.capacity:
            # Poda por factibilidad: Verifica si es posible incluir el elemento actual
            self.selected_items[index] = 1
            max_value_with, total_weight_with = self.knapsack_backtracking(
                current_weight + self.weights[index],
                current_value + self.values[index],
                index + 1
            )
            self.selected_items[index] = 0
             #Intenta excluir el elemento actual de la mochila
            max_value_without, total_weight_without = self.knapsack_backtracking(
                current_weight, current_value, index + 1
            )
            if max_value_with > max_value_without:
                self.selected_items[index] = 1
                return max_value_with, total_weight_with
            else:
                self.selected_items[index] = 0
                return max_value_without, total_weight_without
        else:
             #No es posible incluir el elemento actual debido a la capacidad
            return self.knapsack_backtracking(current_weight, current_value, index + 1)
        
    def solve(self):
        max_value, total_weight = self.knapsack_backtracking(0, 0, 0)
        return max_value, total_weight
    def display_selected_items(self):
        print("Elementos seleccionados en la mochila:")
        for i in range(self.n):
            if self.selected_items[i] == 1:
                print(f"Elemento {i + 1} - Peso: {self.weights[i]}, Valor: {self.values[i]}")
# Ejemplo de uso
knapsack_problem = Knapsack(weights, values, capacity)
max_value, total_weight = knapsack_problem.solve()
print(f"Valor máximo en la mochila: {max_value}")
print(f"Peso total en la mochila: {total_weight}")
knapsack_problem.display_selected_items()