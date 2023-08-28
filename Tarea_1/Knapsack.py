from problem import PriorityQueue

with open('ks_19_0', 'r') as file:
       first_line19 = file.readline().split()
       num_elements19 = int(first_line19[0])
       capacity19 = int(first_line19[1])
       
       items19 = {}
       for _ in range(num_elements19):
           v, w = map(int, file.readline().split())
           items19[v] = (v,w)

with open('ks_10000_0', 'r') as file:
       first_line10000 = file.readline().split()
       num_elements10000 = int(first_line10000[0])
       capacity10000 = int(first_line10000[1])
       
       items10000 = {}
       for _ in range(num_elements10000):
           v, w = map(int, file.readline().split())
           items10000[v] = (v,w)

# Simple heuristic: value-to-weight ratio
def heuristic(items):
    heuristic = {}
    for i in items.keys():
        (v, w) = items[i]
        heuristic[i] = v/w 
    return heuristic

heuristic19 = heuristic(items19)
heuristic10000 = heuristic(items10000)


def knapsack_GS(items, capacity, heuristic):
    
    knapsack = []  # Initial state is an empty knapsack
    current_value = 0
    frontier = PriorityQueue()
    
    for item in items.keys():
        frontier.push((item, items[item]), -heuristic[item])
    explored = set()

    while frontier._elements:
        (item, (item_added,weight)) = frontier.pop()
        explored.add(item)  

        
        if weight<=capacity:
            if (current_value + weight) <= capacity:
                knapsack.append((item_added,weight))
                current_value += weight

    print('Algoritmo usado: Búsqueda Voraz')
    print(f'Cantidad de Objetos en la Mochila: {len(knapsack)}' )
    print(f'Capacidad de la mochila: {capacity} g')
    print(f'Peso total conseguido: {current_value}')
    print(f'Capacidad sin utilizar: {capacity-current_value}')
    print(f'Mochila: {knapsack}')

    return True


#knapsack_GS(items19,capacity19, heuristic19)
knapsack_GS(items10000,capacity10000,heuristic10000)

