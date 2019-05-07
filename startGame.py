## Javier Huertas (2017-18)
## Alejandro Cervantes (2017-18)
'''startGame.py
   Artificial Intelligence Course
   Practice on Space State Search
   Loads the module paths and calls the main graphic interface

   Run this script from the extraction folder
'''

import os,sys

sys.path.append(os.path.abspath("./student"))
sys.path.append(os.path.abspath("./game"))
sys.path.append(os.path.abspath("./simpleai-0.8.1"))

import gameAI


# Functions to be implemented
def action(self, state):
    '''
        Retrieves the list of applicable actions from a state.
    '''
result = None

return result

#############################

def result(self, state, action):
    '''
        Retrieves the outcome of applying an action to a state.
    '''
result = None

return result

#############################

def is_goal(self, state, action):
    '''
        Retrieves TRUE if the state is the goal state, false otherwise.
    '''
result = None

return result

#############################

def cost(source_state, target_state, action):
    '''
        Retrieves the cost of achieving target state from source applying action.
    '''
result = None

return result

#############################

def heuristic(state):
    '''
        Retrieves the estimated cost of reaching the goal from a given state.
    '''
result = None

return result

#############################

def setup():
    '''
        Configures the initial state, the goal state, and the search algorithm.
    '''
result = None

return result

#############################

def printState(state):
    '''
        Prints the value of a state in the interface.
    '''
result = None

return result

#############################

def getPendingRequests(state):
    '''
        Returns the number of pending orders to the delivery location.
    '''
result = None

return result
