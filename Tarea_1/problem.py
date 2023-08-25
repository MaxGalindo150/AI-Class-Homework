
import re
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
    
    def print_path(self, l):
        print('-->'.join(l))
    



# Graphs

Graph = {
    'Arad': {'GoSibiu': 'Sibiu', 'GoZerind': 'Zerind', 'GoTimisoara': 'Timisoara'},
    'Bucharest': {'GoGiurgiu': 'Giurgiu', 'GoFagaras': 'Fagaras', 'GoPitesti': 'Pitesti', 'GoUrziceni': 'Urziceni'},
    'Craiova': {'GoDobreta': 'Dobreta', 'GoPitesti': 'Pitesti', 'GoRimnicu Vilcea': 'Rimnicu Vilcea'},
    'Dobreta': {'GoCraiova': 'Craiova', 'GoMehadia': 'Mehadia'},
    'Eforie': {'GoHirsova': 'Hirsova'},
    'Fagaras': {'GoBucharest': 'Bucharest', 'GoSibiu': 'Sibiu'},
    'Giurgiu': {'GoBucharest': 'Bucharest'},
    'Hirsova': {'GoEforie': 'Eforie', 'GoUrziceni': 'Urziceni'},
    'Iasi': {'GoNeamt': 'Neamt', 'GoVaslui': 'Vaslui'},
    'Lugoj': {'GoMehadia': 'Mehadia', 'GoTimisoara': 'Timisoara'},
    'Mehadia': {'GoDobreta': 'Dobreta', 'GoLugoj': 'Lugoj'},
    'Neamt': {'GoIasi': 'Iasi'},
    'Oradea': {'GoSibiu': 'Sibiu', 'GoZerind': 'Zerind'},
    'Pitesti': {'GoBucharest': 'Bucharest', 'GoCraiova': 'Craiova', 'GoRimnicu Vilcea': 'Rimnicu Vilcea'},
    'Rimnicu Vilcea': {'GoCraiova': 'Craiova', 'GoPitesti': 'Pitesti', 'GoSibiu': 'Sibiu'},
    'Sibiu': {'GoArad': 'Arad', 'GoFagaras': 'Fagaras', 'GoOradea': 'Oradea', 'GoRimnicu Vilcea': 'Rimnicu Vilcea'},
    'Timisoara': {'GoArad': 'Arad', 'GoLugoj': 'Lugoj'},
    'Urziceni': {'GoBucharest': 'Bucharest', 'GoHirsova': 'Hirsova', 'GoVaslui': 'Vaslui'},
    'Vaslui': {'GoIasi': 'Iasi', 'GoUrziceni': 'Urziceni'},
    'Zerind': {'GoArad': 'Arad', 'GoOradea': 'Oradea'}
}

G_cost = {
    'Arad': {'Sibiu':140,'Zerind': 75, 'Timisoara': 118},
    'Bucharest':{'Giurgiu': 90, 'Fagaras': 211,'Pitesti': 101,'Urziceni': 85},
    'Craiova':{'Dobreta': 120, 'Pitesti': 138,'Rimnicu Vilcea': 146},
    'Dobreta':{'Craiova': 120, 'Mehadia': 75},
    'Eforie':{'Hirsova': 86},
    'Fagaras':{'Bucharest': 211, 'Sibiu': 99},
    'Giurgiu':{'Bucharest': 90},
    'Hirsova':{'Eforie': 86,'Urziceni': 98},
    'Iasi':{'Neamt': 87,'Vaslui': 92},
    'Lugoj':{'Mehadia': 70, 'Timisoara': 111},
    'Mehadia':{'Dobreta': 75, 'Lugoj': 70},
    'Neamt':{'Iasi': 87},
    'Oradea':{'Sibiu': 151, 'Zerind': 71},
    'Pitesti':{'Bucharest': 101, 'Craiova': 138, 'Rimnicu Vilcea': 97},
    'Rimnicu Vilcea':{'Craiova': 146, 'Pitesti': 97, 'Sibiu': 80},
    'Sibiu':{'Arad': 140, 'Fagaras': 99, 'Oradea': 151,'Rimnicu Vilcea': 80},
    'Timisoara':{'Arad': 118,'Lugoj': 111},
    'Urziceni':{'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Vaslui':{'Iasi': 92,'Urziceni': 142},
    'Zerind':{'Arad': 75, 'Oradea': 71}
}




