
'''
    Class gameProblem, implements simpleai.search.SearchProblem
'''


from simpleai.search import SearchProblem

# TODO: I suppose this part is used on the second part of the assignment.
# from simpleai.search import breadth_first,depth_first,astar,greedy

import simpleai.search

class GameProblem(SearchProblem):

    # Object attributes, can be accessed in the methods below

    MAP = None
    POSITIONS = None
    INITIAL_STATE = None
    GOAL = None
    CONFIG = None
    AGENT_START = None
    SHOPS = None
    CUSTOMERS = None
    MAXBAGS = 0

    MOVES = ('West','North','East','South')

   # --------------- Common functions to a SearchProblem -----------------

    X = 0
    Y = 1

    def actions(self, state):
        '''Returns a LIST of the actions that may be executed in this state
        '''
        actions = []

        # Retrieve the state information into the dictionary stateDate.
        stateData = getStateData(self, state)
        # Actual Position now holds a tuple which can be indexed like a list.
        actualPosition = self.POSITIONS

        # Check NORTH
        if(actualPosition[Y] - 1 > 0):
            northPosition = (actualPosition[X], actualPosition[Y] - 1)
            position_marker = getAttribute(self, northPosition, 'marker')
            if (position_marker != 'X'):
                actions.append('North')

        # Check EAST
        if(actualPosition[X] + 1 < CONFIG['map_size'][X] - 1):
            eastPosition = (actualPosition[X] + 1, actualPosition[Y])
            position_marker = getAttribute(self, eastPosition, 'marker')
            if (position_marker != 'X'):
                actions.append('East')

        # Check WEST
        if(actualPosition[X] - 1 > 0):
            westPosition = (actualPosition[X] - 1, actualPosition[Y])
            position_marker = getAttribute(self, westPosition, 'marker')
            if (position_marker != 'X'):
                actions.append('West')

        # Check SOUTH
        if(actualPosition[Y] + 1 < CONFIG['map_size'][Y] - 1):
            southPosition = (actualPosition[X], actualPosition[Y] + 1)
            position_marker = getAttribute(self, southPosition, "marker")
            if (position_marker != 'X'):
                actions.append('South')

        return actions


    def result(self, state, action):
        '''Returns the state reached from this state when the given action is executed
        '''
        next_state = 0

        return next_state


    def is_goal(self, state):
        '''Returns true if state is the final state
        '''

        # Final state is defined as the state where the deliverer is back at the Start
        # and all pizzas have been delivered
        return True

    def cost(self, state, action, state2):
        '''Returns the cost of applying `action` from `state` to `state2`.
           The returned value is a number (integer or floating point).
           By default this function returns `1`.
        '''
        return 1

    def heuristic(self, state):
        '''Returns the heuristic for `state`
        '''
        return 0


    def setup (self):
        '''This method must create the initial state, final state (if desired) and specify the algorithm to be used.
           This values are later stored as globals that are used when calling the search algorithm.
           final state is optional because it is only used inside the is_goal() method

           It also must set the values of the object attributes that the methods need, as for example, self.SHOPS or self.MAXBAGS
        '''
        self.CONFIG = None
        self.MAP = None
        self.POSITIONS = None

        print '\nMAP: ', self.MAP, '\n'
        print 'POSITIONS: ', self.POSITIONS, '\n'
        print 'CONFIG: ', self.CONFIG, '\n'

        # We define the state as a tuple containing a mix of tuples and lists.
        # These tuples/lists are the following entities:
        #   - Deliverer                                 (tuple)
        #       > Coordinates (x, y)                    (list)
        #       > # Loaded Pizzas (0:2)                 (list of 1 elem)
        #   - Clients (n clients)                       (tuple)
        #       > Coordinates (x, y)                    (tuple)
        #       > # Pizzas yet to be recieved (0:3)     (list of 1 elem)
        #   - Pizza Shops (n pizza shops)               (tuple)
        #       > Coordinates (x, y)                    (tuple)

        # TODO: NOW INSTEAD OF HAVING THIS VARIABLES HARD-CODED, GET THEM FROM CONFIG
        initial_state = (
            ([0, 0], [0]), # Deliverer
            ((9, 1), [1]), # Client 1
            ((3, 3), [1]), # Client 2
            ((4, 3), [2]), # Client 3
            ((6, 0)) # Pizza Shop 1
        )

        final_state =  (
            ([0, 0], [0]), # Deliverer
            ((9, 1), [0]), # Client 1
            ((3, 3), [0]), # Client 2
            ((4, 3), [0]), # Client 3
            ((6, 0)) # Pizza Shop 1
        )

        algorithm = simpleai.search.astar

        # TODO: Then again, here are the other search algorithms.

        #algorithm= simpleai.search.breadth_first
        #algorithm= simpleai.search.depth_first
        #algorithm= simpleai.search.limited_depth_first

        return initial_state,final_state,algorithm

    def printState (self,state):
        '''Return a string to pretty-print the state '''
        pps=''
        # Iterate through the 

        return (pps)

    def getPendingRequests (self,state):
        ''' Return the number of pending requests in the given position (0-N).
            MUST return None if the position is not a customer.
            This information is used to show the proper customer image.
        '''
        return None

    # -------------------------------------------------------------- #
    # --------------- DO NOT EDIT BELOW THIS LINE  ----------------- #
    # -------------------------------------------------------------- #

    def getAttribute (self, position, attributeName):
        '''Returns an attribute value for a given position of the map
           position is a tuple (x,y)
           attributeName is a string

           Returns:
               None if the attribute does not exist
               Value of the attribute otherwise
        '''
        tileAttributes=self.MAP[position[0]][position[1]][2]
        if attributeName in tileAttributes.keys():
            return tileAttributes[attributeName]
        else:
            return None

    def getStateData (self,state):
        stateData={}
        pendingItems=self.getPendingRequests(state)
        if pendingItems >= 0:
            stateData['newType']='customer{}'.format(pendingItems)
        return stateData

    # THIS INITIALIZATION FUNCTION HAS TO BE CALLED BEFORE THE SEARCH
    def initializeProblem(self,map,positions,conf,aiBaseName):
        self.MAP=map
        self.POSITIONS=positions
        self.CONFIG=conf
        self.AGENT_START = tuple(conf['agent']['start'])

        initial_state,final_state,algorithm = self.setup()
        if initial_state == False:
            print ('-- INITIALIZATION FAILED')
            return True

        self.INITIAL_STATE=initial_state
        self.GOAL=final_state
        self.ALGORITHM=algorithm
        super(GameProblem,self).__init__(self.INITIAL_STATE)

        print ('-- INITIALIZATION OK')
        return True

    # END initializeProblem
