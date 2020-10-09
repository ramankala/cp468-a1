import copy 

GOALSTATE = []


def initialState(size):
    """
    Returns the initial state of the puzzle 
    """
    pass


def blankSpot(puzzle):
    """
    returns the indix (i, j) of where the blank spot is 
    """
    temp = copy.deepcopy(puzzle)
    length = len(temp) - 1

    for i in range(0, length):
        for j in range(0, length):
            if temp[i][j] == None:
                return i, j 



def actions(puzzle):
    """
    Returns set of all possible actions available on the puzzle 
    """
    temp = copy.deepcopy(puzzle)
    length = len(temp) - 1

    acts = set() 

    # find the blank spot 
    row_blank, col_blank = blankSpot(temp)

    if (row_blank + 1) <= 2:
        acts.add((row_blank + 1, col_blank))
        # if (col_blank + 1) <= 



def result(puzzle, act, blank):
    """
    Takes in the action (move) and does it on the puzzle. 
    -------------------------------------------------------
    Parameters:
        puzzle: the puzzle state that the act is to be done on 
        act: a tuple (i, j) with the coordinates (indix) of the sport we can switch with the blank spot 
        blank: where the blank spot is in the puzzle  (i, j)
    Return: 
        puzzle state after moving the blank spot to the act 
    """

    temp = copy.deepcopy(puzzle)

    row0 = act[0]
    col0 = act[1]
    row1 = blank[0]
    col1 = blank[1]

    numAct = temp[row0][col0]
    blank1 = temp[row1][col1]

    temp[row0][col0] = blank1
    temp[row1][col1] = numAct

    return temp


def h1(currentState, GOALSTATE):
    """
    Takes current state and goal state of puzzle. Then calculates the number of misplaced tiles. 
    ---------------------------------------------------------------------------------------------
    Parameteres:
        currentState: current state of the puzzle 
        goalState: goal state of the puzzle we are trying to achieve 
    """

    length = len(currentState)

    for i in range(0, length):
        for j in range(0, length):
            if (currentState[i][j] != GOALSTATE[i][j]):
                misplacedTiles += 1 

    return misplacedTiles 


def puzzleSolved(puzzle):
    """ 
    Returns whether the puzzle is solved or not 
    """
    
    temp = h1(puzzle, GOALSTATE)

    if (temp == 0):
        solved = True
    else: 
        solved = False

    return solved


def h2(currentState, GOALSTATE):
    """
    Manhatton Distance 
    """
    pass