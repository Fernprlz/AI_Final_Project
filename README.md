# AI_Final_Project

---

## Progress:
  * actions             **[OK!]**
  * result              **[OK!]**
  * is_goal             **[OK!]**
  * cost
  * heuristic
  * setup               **[OK!]**
  * printState
  * getPendingRequests

## Submission:
  ZIP: *pr-ai-2019-100383461-100383462.zip*
  * Report
    * Introduction.
    * Description and explanation of the solution.
    * Description and explanation of the tests.
    * Conclusions
    * Personal Comments.
  * Directory: *pr-ia-2019/student-code*

## Questions:
  * There can be 'n' number of clients.
  * There can be 'n' number of pizza shops.
  * How do the algorithms interact with our class.
  * Do we need to check again if an action is valid on the 'result' function?

## Notes:
  * MAP is a list of 4 positions. The 2 first indexes represent the coordinates of a tile
  in the map. The third one represents the data you want to retrieve:
    * [0] - Type of tile (street, whatever)
    * [1] - ID of the tile. A number assigned for every tile of the same type. (A tile
      can be the 5th street tile, therefore its ID is 5).
    * [2] - Attributes (dictionary with the cost and some data depending on the tile type)
    * [3] - State (dictionary stating if there's an agent on the tile and if the image has to
    be other than default).
  * POSITIONS is a dictionary saving the positions of all tiles per type of tile. There are
  7 keys on the dictionary:
    * 'building'
    * 'customer1'
    * 'customer2'
    * 'agent'
    * 'start'
    * 'street'
    * 'pizza'
  * STATES are tuples. type(initial_state) returns "tuple", but we have to design the contents.

  ------

### Definition of State

We define the state as a tuple containing a mix of tuples and lists.
These tuples/lists are the following entities:
  - Deliverer                               (tuple)
    - Coordinates (x, y)                    (list)
    - ºLoaded Pizzas (0:2)                 (list of 1 elem)
  - Clients                                 (list)
    - (n clients)                           (tuple)
      - Coordinates (x, y)                  (tuple
      - ºPizzas yet to be recieved (0:3)   (list of 1 elem)
  - Pizza Shops                             (list)
    - (n pizza shops)                       (list)
      - Coordinates (x, y)                  (tuple)

### Credits for the images:
  * Buildings:
    * Icons made by https://www.flaticon.com/authors/dinosoftlabs
  DinosoftLabs from https://www.flaticon.com is licensed by Creative Commons BY 3.0
  * Pizza shop:
    * <a href="https://www.freepik.com/free-photos-vectors/flower">Flower vector created by rawpixel.com - www.freepik.com</a>
