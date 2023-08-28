from problem import Problem, Graph # Import the Class Problem and the graph

def DLS(problem, depth_limit):
    return recursive_DLS(problem.initial_state, problem, depth_limit)

def recursive_DLS(node, problem, depth_limit):
    
    if problem.is_goal(node):
        return [node]
    
    if depth_limit == 0:
        return None
    
    
    cutoff_occurred = False #cutoff false

    
    for action in problem.actions[node].keys():
        (child,_) = problem.result(node, action)
        result = recursive_DLS(child, problem, depth_limit - 1)
        
        if result == 'cutoff':
            cutoff_occurred = True #Change cutoff state
        elif result is not None:
            problem.print_path([node] + result)
            return [node] + result
    
    if cutoff_occurred:
        return 'cutoff'
    else:
        return None
 

def iterative_search(problem, max_depth):
    for depth in range(max_depth + 1):
        if DLS(problem, depth):
            return True
    return False


# Example problem instantiation
arad_to_bucharest = Problem('Arad', ['Bucharest'], Graph)
iterative_search(arad_to_bucharest, 10)
