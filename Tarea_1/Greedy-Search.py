from problem import Problem, PriorityQueue, Graph, heuristics

def GS(problem, heuristic):
    node = problem.initial_state
    frontier = PriorityQueue()
    frontier.push((node, [], 0), heuristic[node])  # Tuple format: (node, path, current_cost)
    explored = set()

    while frontier._elements:
        (node, path, current_cost) = frontier.pop()  # Including current_cost in the tuple
        explored.add(node)

        if problem.is_goal(node):
            problem.print_path(path + [node])
            print("Total Cost:", current_cost)  # Print the accumulated cost of the path
            return True

        for action in problem.actions[node].keys():
            (child, action_cost) = problem.result(node, action)
            
            new_cost = current_cost + action_cost  # Calculate the accumulated cost for the child
            if child not in explored and child not in {node for _, _, _ in frontier._elements}:
                frontier.push((child, path + [node], new_cost), heuristic[child])  # Use heuristic for priority

    return False  # No solution found

problem = Problem('Arad', ['Bucharest'], Graph)
GS(problem, heuristics)
