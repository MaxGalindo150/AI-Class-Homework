
import heapq

# Problem 
class Problem:
    def __init__(self, initial_state, goal_test, actions):
        """
        In this class we have the definition of our problem:
        -Initial State: The first node of our graph.
        -Goal test: This is given by the desired node.
        -Actions: The actions in our problem.
        """
        self.initial_state = initial_state
        self.goal_test = goal_test
        self.actions = actions

    def __str__(self):
        """
        This is for clarify the initial state and the goal.
        """
        msg = "Initial State: {0} -> Goal: {1}"
        return msg.format(self.initial_state,
                          self.goal_test)

    def is_goal(self, state):
        """
        This method helps us to know if we are at the desired node.
        """
        return state in self.goal_test

    def result(self, state, action):
        """
        This is our successor function. It means that if we give to result(state, action) an action
        at some state then this function returns a new state.
        """
        if state not in self.actions.keys(): # This checks if our current status has actions
            return None
        
        actions_in_state = self.actions[state] # We bring available actions of our state
        
        if action not in actions_in_state.keys(): #This checks if the action is in the available actions.
            return None
        
        return actions_in_state[action]
    
    def print_path(self, path):
        print('-->'.join(path))






    
#Priority Queue
class PriorityQueue:
    def __init__(self):
        self._elements = []
        self._index = 0  # To manage elements with the same priority 

    def push(self, item, priority):
        heapq.heappush(self._elements, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._elements)[-1]

# Graph

Graph = {
    'Arad': {'GoSibiu': ('Sibiu',140), 'GoZerind': ('Zerind',75), 'GoTimisoara': ('Timisoara',118)},
    'Bucharest': {'GoGiurgiu': ('Giurgiu',90), 'GoFagaras': ('Fagaras',211), 'GoPitesti': ('Pitesti',101), 'GoUrziceni': ('Urziceni',85)},
    'Craiova': {'GoDobreta':('Dobreta',120), 'GoPitesti': ('Pitesti',138), 'GoRimnicu Vilcea': ('Rimnicu Vilcea',146)},
    'Dobreta': {'GoCraiova': ('Craiova',120), 'GoMehadia': ('Mehadia',75)},
    'Eforie': {'GoHirsova': ('Hirsova',86)},
    'Fagaras': {'GoBucharest': ('Bucharest',211), 'GoSibiu': ('Sibiu',99)},
    'Giurgiu': {'GoBucharest': ('Bucharest',90)},
    'Hirsova': {'GoEforie': ('Eforie',86), 'GoUrziceni': ('Urziceni',98)},
    'Iasi': {'GoNeamt': ('Neamt',87), 'GoVaslui': ('Vaslui',92)},
    'Lugoj': {'GoMehadia': ('Mehadia',70), 'GoTimisoara': ('Timisoara',111)},
    'Mehadia': {'GoDobreta': ('Dobreta',75), 'GoLugoj': ('Lugoj',70)},
    'Neamt': {'GoIasi': ('Iasi',87)},
    'Oradea': {'GoSibiu': ('Sibiu',151), 'GoZerind': ('Zerind',71)},
    'Pitesti': {'GoBucharest': ('Bucharest',101), 'GoCraiova': ('Craiova',138), 'GoRimnicu Vilcea': ('Rimnicu Vilcea',97)},
    'Rimnicu Vilcea': {'GoCraiova': ('Craiova',146), 'GoPitesti': ('Pitesti',97), 'GoSibiu': ('Sibiu',80)},
    'Sibiu': {'GoArad': ('Arad',140), 'GoFagaras': ('Fagaras',99), 'GoOradea': ('Oradea',151), 'GoRimnicu Vilcea': ('Rimnicu Vilcea',80)},
    'Timisoara': {'GoArad': ('Arad',118), 'GoLugoj': ('Lugoj',111)},
    'Urziceni': {'GoBucharest': ('Bucharest',85), 'GoHirsova': ('Hirsova',98), 'GoVaslui': ('Vaslui',142)},
    'Vaslui': {'GoIasi': ('Iasi',92), 'GoUrziceni': ('Urziceni',142)},
    'Zerind': {'GoArad': ('Arad',75), 'GoOradea': ('Oradea',71)}
}

heuristics = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Dobreta': 242,
    'Eforie': 161,
    'Fagaras': 178,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 98,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}




