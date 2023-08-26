from problem import Problem, PriorityQueue, Graph, heuristics

def GS(problem, heuristic):
    node = problem.initial_state
    frontier = PriorityQueue()
    frontier.push((node, [], 0), heuristic[node])  # Tuple format: (node, path, heuristic_value)
    explored = set()

    while frontier._elements:
        (node, path, _) = frontier.pop()  # Removed heuristic from the tuple
        explored.add(node)

        if problem.is_goal(node):
            problem.print_path(path + [node]) 
            return True

        for action in problem.actions[node].keys():
            (child, cost) = problem.result(node, action)
            
            if child not in explored and child not in {node for _, _, _ in frontier._elements}:
                frontier.push((child, path + [node], 0), heuristic[child])  # Heuristic value used for priority

    return False  # No solution found


problem = Problem('Arad', ['Bucharest'], Graph)
GS(problem, heuristics)
