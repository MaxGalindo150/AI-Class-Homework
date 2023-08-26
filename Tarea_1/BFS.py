from problem import Problem, Graph # Import the Class Problem and the graph

def BFS(problem):
    node = problem.initial_state
    
    if problem.is_goal(node):
        print(f'You are already at the goal: {node}')
        return True
    
    frontier = [(node, [node])]
    explored = set()
    
    while frontier:
        (node, path) = frontier.pop(0) # Using pop() for DFS behavior (FIFO)
        explored.add(node)

        if problem.is_goal(node):
            problem.print_path(path)
            return True
        
        for action in problem.actions[node].keys():
            child = problem.result(node, action)
            if child not in explored and child not in [nodes_in_frontier for nodes_in_frontier, _ in frontier]:
                frontier.append((child, path + [child]))

    print('No solution was found')
    return False

# Example problem instantiation
arad_to_bucharest = Problem('Arad', ['Bucharest'], Graph)
BFS(arad_to_bucharest)
