from problem import Problem, Graph, PriorityQueue # Import the Class Problem and the graph

def UCS(problem):
    node = problem.initial_state
    frontier = PriorityQueue()
    frontier.push((node, [], 0), 0)  # Tuple format: (node, path, cost)
    explored = set()

    while frontier._elements:
        (node, path, current_cost) = frontier.pop()
        explored.add(node)

        if problem.is_goal(node):
            problem.print_path(path + [node]) 
            print(f'Total Cost: {current_cost}')         # Print path including the current node
            return True

        for action in problem.actions[node].keys():
            (child, cost) = problem.result(node, action)
            
            new_cost = current_cost + cost
            if child not in explored and child not in {node for _, _, _ in frontier._elements}:
                frontier.push((child, path + [node], new_cost), new_cost)

    return False  # No solution found

problem = Problem('Arad', ['Bucharest'], Graph)
UCS(problem)
