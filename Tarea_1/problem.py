#Action
class Action:
    def __init__(self, name):
        """Each action needs its name"""
        self.name = name

    def __str__(self):
        return self.name

#State
class State:
    def __init__(self, name, actions):
        """
        Since in each state you can do different actions,
        we added the actions parameter.
        """
        self.name = name
        self.actions = actions

    def _str_(self):
        return self.name
    
#Problem 
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
        if state.name not in self.actions.keys(): # This checks if our current status has actions
            return None
        
        actions_in_state = self.actions[state.name] # We bring available actions of our state
        
        if action.name not in actions_in_state.keys(): #This checks if the action is in the available actions.
            return None
        
        return actions_in_state[action.name]