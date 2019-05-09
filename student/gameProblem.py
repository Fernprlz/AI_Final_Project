
'''
    Class gameProblem, implements simpleai.search.SearchProblem
'''

from copy import deepcopy
from simpleai.search import SearchProblem

# TODO: I suppose this part is used on the second part of the assignment.
# from simpleai.search import breadth_first,depth_first,astar,greedy

import simpleai.search

final_state = None
tile_type = 0
tile_ID = 1
tile_Attr = 2
tile_State = 3
X = 0
Y = 1

deliverer = 0
coords = 0
customers = 1
pipsas = 1

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

    def actions(self, state):
        '''Returns a LIST of the actions that may be executed in this state
        '''
        actions = []

        ######### Check NORTH #########

        next_X = self.POSITIONS['agent'][0][X]
        next_Y = self.POSITIONS['agent'][0][Y] - 1
        if (self.POSITIONS['agent'][0][Y] - 1 > 0 and self.MAP[next_X][next_Y][tile_type] != 'building'):
                actions.append('North')

        ######### Check SOUTH #########
        next_X = self.POSITIONS['agent'][0][X]
        next_Y = self.POSITIONS['agent'][0][Y] + 1
        if (self.POSITIONS['agent'][0][Y] + 1 <= self.CONFIG['map_size'][Y] - 1 and self.MAP[next_X][next_Y][tile_type] != 'building'):
                actions.append('South')

        ######### Check WEST #########
        next_X = self.POSITIONS['agent'][0][X] - 1
        next_Y = self.POSITIONS['agent'][0][Y]
        if (self.POSITIONS['agent'][0][X] - 1 > 0 and self.MAP[next_X][next_Y][tile_type] != 'building'):
                actions.append('West')

        ######### Check EAST #########
        next_X = self.POSITIONS['agent'][0][X] + 1
        next_Y = self.POSITIONS['agent'][0][Y]
        if (self.POSITIONS['agent'][0][X] + 1 <= self.CONFIG['map_size'][X] - 1 and self.MAP[next_X][next_Y][tile_type] != 'building'):
                actions.append('East')

        ######### Check LOAD #########
        if (self.POSITIONS['agent'][0] in self.POSITIONS['pizza']):
            actions.append('Load')

        ######## Check UNLOAD #########
        if (self.POSITIONS['agent'][0] in state[customers] and getAttribute(self, self.POSITIONS['agent'][0], 'object') > 0):
            actions.append('Unload')

        return actions

    def result(self, state, action):
               '''Returns the state reached from this state when the given action is executed
        '''
		# POSITIONS: {
		#'building': [(1, 3), (2, 0), (3, 2), (4, 1), (6, 1)],
		#'customer1': [(9, 1), (9, 3)],
		#'customer2': [(4, 3)],
		#'agent': [(0, 0)],
		#'start': [(0, 0)],
		#'street': [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 3), (4, 0), (4, 2), (5, 0), (5, 1), (5, 2), (5, 3), (6, 2), (6, 3), (7, 0), (7, 1), (7, 2), (7, 3), (8, 0), (8, 1), (8, 2), (8, 3), (9, 0), (9, 2)],
		#'pizza': [(6, 0)]
		# }
        next_state = 0

	#First option: North
        if (action=='North'):
            #Update deliverer coordinates
		    next_delCords = (state[deliverer][coords][X], state[deliverer][coords][Y] - 1)
		#Create next state to return
		next_delState = (next_delCords, state[deliverer][pipsas])
		next_state = next_delState + state[customers]

        #Second option: East
        if (action=='East'):
            #Update deliverer coordinates
            next_delCords = (state[deliverer][coords][X]+1, state[deliverer][coords][Y])
            #Create next state to return
		next_delState = (next_delCords, state[deliverer][pipsas])
		next_state = next_delState + state[customers]

        #Third option: South
        if (action=='South'):
            #Update deliverer coordinates
            next_delCords = (state[deliverer][coords][X], state[deliverer][coords][Y]+1)
            #Create next state to return
		next_delState = (next_delCords, state[deliverer][pipsas])
		next_state = next_delState + state[customers]

        #Fourth option: West
        if (action=='West'):
            #Update deliverer coordinates
            next_delCords = (state[deliverer][coords][X]-1, state[deliverer][coords][Y])
            #Create next state to return
		next_delState = (next_delCords, state[deliverer][pipsas])
		next_state = next_delState + state[customers]

	#Fifth option: Load
	if (action=='Load'):
		#Update deliverer's loaded pizzas
		next_delPizzas = states[deliverer][pipsas]+1
		#Create next state to return
		next_delState = (state[deliverer][coords], next_delPizzas)
		next_state = next_delState + state[customers]

	#Sixth option: Unload
	if (action=='Unload'):
		#Update client's pending orders
		next_clientPizzas = ()
		next_clientN = ()
		next_clientState = ()
		for n in range len(state[customers]):
			if cmp(state[customers][n][coords], state[deliverer][coords]) == 0:
				next_clientPizzas += (state[customers][n][pipsas]-1)
				next_clientN +
			else:
				next_clientState += state[customers][n]

		#Create next state to return


		#if getAttribute(self, next_delCords, 'objects') != None:

        return next_state

    def is_goal(self, state):
        '''Returns true if state is the final state
        '''
        result = False

        # Final state is defined as the state where the deliverer is back at the Start
        # and all pizzas have been delivered
        if (state == final_state):
            result = True

        return result

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

        print '\nMAP: ', self.MAP, '\n'
        print 'POSITIONS: ', self.POSITIONS, '\n'
        print 'CONFIG: ', self.CONFIG, '\n'

        # ==================== I N I T I A L _ S T A T E  ==================== #

        ############# Create the Deliverer #############
        # Create the list of coordinates. We chose a list because the agent will change positions.
        del_Coords = self.POSITIONS['start'][0]
        # At the beginning no pizzas are loaded.
        deliverer = (del_Coords, 0)

        ############# Create the Customers #############
        customers = ()
        if ('customer1' in self.POSITIONS):
            for coords in self.POSITIONS['customer1']:
                customers += (
                                coords, # Coordinates of the client
                                self.MAP[coords[X]][coords[Y]][tile_Attr]['objects'] # Number of orders
                             )
        if ('customer2' in self.POSITIONS):
            for coords in self.POSITIONS['customer2']:
                customers += (
                                coords, # Coordinates of the client
                                self.MAP[coords[X]][coords[Y]][tile_Attr]['objects'] # Number of orders
                             )
        if ('customer3' in self.POSITIONS):
            for coords in self.POSITIONS['customer3']:
                customers += (
                                coords, # Coordinates of the client
                                self.MAP[coords[X]][coords[Y]][tile_Attr]['objects'] # Number of orders
                             )

        ######### Join the initial_state tuple #########
        initial_state = deliverer + customers

        # ====================== F I N A L _ S T A T E  ====================== #

        ############# Create the Deliverer #############
        # No pizzas loaded and deliverer back at the start position
        del_Coords = self.POSITIONS['start'][0]
        deliverer = (del_Coords, 0)

        ############# Create the Customers #############
        # No orders left to deliver
        customers = ()
        if ('customer1' in self.POSITIONS):
            for coords in self.POSITIONS['customer1']:
                customers += (coords, 0)

        if ('customer2' in self.POSITIONS):
            for coords in self.POSITIONS['customer2']:
                customers += (coords, 0)

        if ('customer3' in self.POSITIONS):
            for coords in self.POSITIONS['customer3']:
                customers += (coords, 0)

        final_state = deliverer + customers

        # ==================================================================== #

        algorithm = simpleai.search.astar

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
