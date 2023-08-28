from problem import Problem, PriorityQueue, Graph, heuristics # Import the Class Problem and the graph

def a_star_search(problem, heuristic):
    node = problem.initial_state
    frontier = PriorityQueue()
    frontier.push((node, [], 0), heuristic[node])  # Tuple format: (node, path, g_cost)
    explored = set()

    while frontier._elements:
        (node, path, g_cost) = frontier.pop()  
        explored.add(node)

        if problem.is_goal(node):
            problem.print_path(path + [node])
            print(f'Total Cost: {g_cost}')
            return True

        for action in problem.actions[node].keys():
            (child, cost) = problem.result(node, action)
            
            new_g_cost = g_cost + cost
            if child not in explored and child not in {node for _, _, _ in frontier._elements}:
                f_cost = new_g_cost + heuristic[child]  # Calculate f_cost using g and heuristic
                frontier.push((child, path + [node], new_g_cost), f_cost)

    return False  # No solution found

problem = Problem('Arad', ['Bucharest'], Graph)
a_star_search(problem, heuristics)
