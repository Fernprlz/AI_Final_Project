
'''
    Class gameProblem, implements simpleai.search.SearchProblem
'''

from copy import deepcopy
from simpleai.search import SearchProblem

from simpleai.search import breadth_first,depth_first,astar,greedy

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
pizzas = 1

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

        next_X = state[deliverer][coords][X]
        next_Y = state[deliverer][coords][Y] - 1
        if (state[deliverer][coords][Y] - 1 >= 0 and self.MAP[next_X][next_Y][tile_type] != 'building'):
                actions.append('North')

        ######### Check SOUTH #########
        next_X = state[deliverer][coords][X]
        next_Y = state[deliverer][coords][Y] + 1
        if (state[deliverer][coords][Y] + 1 <= self.CONFIG['map_size'][Y] - 1 and self.MAP[next_X][next_Y][tile_type] != 'building'):
                actions.append('South')

        ######### Check WEST #########
        next_X = state[deliverer][coords][X] - 1
        next_Y = state[deliverer][coords][Y]
        if (state[deliverer][coords][X] - 1 >= 0 and self.MAP[next_X][next_Y][tile_type] != 'building'):
                actions.append('West')

        ######### Check EAST #########
        next_X = state[deliverer][coords][X] + 1
        next_Y = state[deliverer][coords][Y]
        if (state[deliverer][coords][X] + 1 <= self.CONFIG['map_size'][X] - 1 and self.MAP[next_X][next_Y][tile_type] != 'building'):
                actions.append('East')

        ######### Check LOAD #########
        # If the deliverer is already at max capacity, he cannot load.
        # DEBUGGING
        #print('DELIVERER LOCATION:')
        #print(self.MAP[state[deliverer][coords][X]][state[deliverer][coords][Y]][tile_type])
        if (self.MAP[state[deliverer][coords][X]][state[deliverer][coords][Y]][tile_type] == 'pizza' and state[deliverer][pizzas] < self.MAXBAGS ):
            actions.append('Load')

        ######## Check UNLOAD #########
        # If the deliverer has no pizzas, he cannot deliver.
        if (state[deliverer][pizzas] > 0):
            # Couldn't use 'in' operator because the tuple has an int, which is not an iterable object
            for customer_number in range(len(state[customers])):
                if (state[deliverer][coords] == state[customers][customer_number][coords] and state[customers][customer_number][pizzas] > 0):
                    actions.append('Unload')
                    break

        # DEBUGGING
        # print('Possible actions from state:')
        # print(state)
        # print(actions)
        return actions

    def result(self, state, action):
        '''Returns the state reached from this state when the given action is executed
        '''
        next_state = ()
        # First option: North
        if (action == 'North'):
            # Update deliverer coordinates
            next_delCords = (state[deliverer][coords][X], state[deliverer][coords][Y] - 1)
            # Create next state to return
            next_delState = (next_delCords, state[deliverer][pizzas])
            next_state = (next_delState,) + (state[customers],)

        # Second option: East
        elif (action == 'East'):
            # Update deliverer coordinates
            next_delCords = (state[deliverer][coords][X] + 1, state[deliverer][coords][Y])
            # Create next state to return
            next_delState = (next_delCords, state[deliverer][pizzas])
            next_state = (next_delState,) + (state[customers],)

        #Third option: South
        elif (action == 'South'):
            # Update deliverer coordinates
            next_delCords = (state[deliverer][coords][X], state[deliverer][coords][Y] + 1)
            # Create next state to return
            next_delState = (next_delCords, state[deliverer][pizzas])
            next_state = (next_delState,) + (state[customers],)

        # Fourth option: West
        elif (action == 'West'):
            # Update deliverer coordinates
            next_delCords = (state[deliverer][coords][X] - 1, state[deliverer][coords][Y])
            # Create next state to return
            next_delState = (next_delCords, state[deliverer][pizzas])
            next_state = (next_delState,) + (state[customers],)

        # Fifth option: Load
        elif (action == 'Load'):
            # Update deliverer's loaded pizzas
            next_delPizzas = state[deliverer][pizzas] + 1
            # Create next state to return
            next_delState = (state[deliverer][coords], next_delPizzas)
            next_state = (next_delState,) + (state[customers],)

        # Sixth option: Unload
        elif (action == 'Unload'):
            # Update deliverer's loaded pizzas
            next_delPizzas = state[deliverer][pizzas] - 1
            # Create next state to return
            next_delState = (state[deliverer][coords], next_delPizzas)
            # Update client's pending orders
            next_clientState = ()
            for n in range(len(state[customers])):
                if (cmp(state[customers][n][coords], state[deliverer][coords]) == 0):
                    next_clientState += ((state[customers][n][coords], state[customers][n][pizzas] - 1),)
                else:
                    next_clientState += ((state[customers][n]),)

            # Create next state to return
            next_state = (next_delState,) + (next_clientState,)

        else:
            next_state = state

        # DEBUGGING
        #print(next_state)

        return next_state

    def is_goal(self, state):
        '''Returns true if state is the final state
        '''
        # Final state is defined as the state where the deliverer is back at the Start
        # and all pizzas have been delivered.
        result = (self.final_state == state)

        return result

    def cost(self, state, action, state2):
        '''Returns the cost of applying `action` from `state` to `state2`.
           The returned value is a number (integer or floating point).
           By default this function returns `1`.
        '''
        result = 1

        #source_module = self.POSITIONS['start'][0][X] + self.POSITIONS['start'][0][Y]
        #target_module = state[deliverer][coords][X] + state[deliverer][coords][Y]

        #result = deliverer_module - start_module;

        return 1

    def heuristic(self, state):
        '''Returns the heuristic for `state`
        '''
        # Define the heuristic as the Manhattan distance from the deliverer to the start
        # Without considering the pizzas yet to be unloaded (Basic Part )
        result = 0

        x_diff = abs(self.POSITIONS['start'][0][X] - state[deliverer][coords][X])
        y_diff = abs(self.POSITIONS['start'][0][Y] - state[deliverer][coords][Y])

        result = x_diff + y_diff

        return result

    def setup (self):
        '''This method must create the initial state, final state (if desired) and specify the algorithm to be used.
           This values are later stored as globals that are used when calling the search algorithm.
           final state is optional because it is only used inside the is_goal() method

           It also must set the values of the object attributes that the methods need, as for example, self.SHOPS or self.MAXBAGS
        '''

        #print '\nMAP: ', self.MAP, '\n'
        #print 'POSITIONS: ', self.POSITIONS, '\n'
        #print 'CONFIG: ', self.CONFIG, '\n'

        # ==================== I N I T I A L _ S T A T E  ==================== #

        ############# Create the Deliverer #############
        # Create the list of coordinates. We chose a list because the agent will change positions.
        del_Coords = self.POSITIONS['start'][0]
        # At the beginning no pizzas are loaded.
        deliverer = (del_Coords, 0)
        # Initialize the maxBags variable
        self.MAXBAGS = self.CONFIG['maxBags']

        ############# Create the Customers #############
        customers = ()
        if ('customer1' in self.POSITIONS):
            for coords in self.POSITIONS['customer1']:
                customers += ((
                                coords, # Coordinates of the client
                                self.MAP[coords[X]][coords[Y]][tile_Attr]['objects'] # Number of orders
                             ),)
        if ('customer2' in self.POSITIONS):
            for coords in self.POSITIONS['customer2']:
                customers += ((
                                coords, # Coordinates of the client
                                self.MAP[coords[X]][coords[Y]][tile_Attr]['objects'] # Number of orders
                             ),)
        if ('customer3' in self.POSITIONS):
            for coords in self.POSITIONS['customer3']:
                customers += ((
                                coords, # Coordinates of the client
                                self.MAP[coords[X]][coords[Y]][tile_Attr]['objects'] # Number of orders
                             ),)

        ######### Join the initial_state tuple #########
        initial_state = (deliverer,) + (customers,)

        # ====================== F I N A L _ S T A T E  ====================== #

        ############# Create the Deliverer #############
        deliverer = (del_Coords, 0)
        ############# Create the Customers #############
        # No orders left to deliver
        customers = ()
        if ('customer1' in self.POSITIONS):
            for coords in self.POSITIONS['customer1']:
                customers += ((coords, 0),)

        if ('customer2' in self.POSITIONS):
            for coords in self.POSITIONS['customer2']:
                customers += ((coords, 0),)

        if ('customer3' in self.POSITIONS):
            for coords in self.POSITIONS['customer3']:
                customers += ((coords, 0),)

        self.final_state = (deliverer,) + (customers,)

        # ==================================================================== #

        # WORKS
        algorithm = simpleai.search.astar

        # WORKS
        #algorithm= simpleai.search.breadth_first

        # WORKS AND IS A SHIT
        #algorithm= simpleai.search.depth_first

        # IDK IF IT WORKS
        #algorithm= simpleai.search.limited_depth_first

        # WORKS AND IS EVEN MUCHISIMO MAS SHIT QUE EL DEPTH
        #algorithm = simpleai.search.greedy

        #DEBUGGING
        print('\n%s' % (self.printState(initial_state)))

        return initial_state,final_state,algorithm

    def printState (self,state):
        '''Return a string to pretty-print the state '''
        pps=''

        # Add deliverer information to the pps
        pps += ('======== D E L I V E R E R    I N F O ======\n')
        pps += ('Deliverer coordinates: %s\n' % (state[deliverer][coords],))
        pps += ('Pizzas loaded: %i\n' % (state[deliverer][pizzas]))
        pps += ('======== C U S T O M E R S    I N F O ======\n')
        # Add customer information
        for customer_number in range(len(state[customers])):
            pps += ('Customer %i coordinates: %s\n' % (customer_number, state[customers][customer_number][coords]))
            pps += ('Customer orders left: %i\n' % (state[customers][customer_number][pizzas]))
            pps += ('============================================\n')

        return (pps)

    def getPendingRequests (self,state):
        ''' Return the number of pending requests in the given position (0-N).
            MUST return None if the position is not a customer.
            This information is used to show the proper customer image.
        '''
        print(state)
        result = None
        for customer_number in range(len(state[customers])):
            # Find corresponding client. If found, update result
            if (cmp(state[deliverer][coords], state[customers][customer_number][coords]) == 0):
                result = state[customers][customer_number][pizzas]

        return result

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
