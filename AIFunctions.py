winCases = [(0,1,2),(0,3,6),(0,4,8),(3,4,5),(6,7,8),(1,4,7),(2,5,8),(2,4,6)]
corners = [0, 2, 6, 8]
edges = [1, 3, 5, 7]
middle = 4
winWeight = 100000
class moveNode():
    def __init__(self, state, val):
        self.weight = val
        self.state = state
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    
class AI():
    def __init__(self, val):
        self.let = val
        
def convertLetPos(boardArr):
    """
    Finds and returns the locations in which the initial X or initial X and O were placed on the board

    Parameters:
        boardArr (list) : List containing values (strings and integers) representing the current state of the board
    """
    state = []
    visited = []
    letPresent = True
    while letPresent:
        letPresent = False
        for i in range(len(boardArr)):
            if boardArr[i] == 'X' and i not in visited:
                state.append(i)
                visited.append(i)
                letPresent = True
                break

        for i in range(len(boardArr)):
            if boardArr[i] == 'O' and i not in visited:
                state.append(i)
                visited.append(i)
                letPresent = True
                break

    return state

def minimax(root, depth, alpha, beta, AIMove, val):
    """
    
    Returns:
        val (int) : Value obtained via minimax algorithm for a possible board state
    """
    if AIMove:
        val = float('-inf')
        for Node in root:
            if len(Node.children) == 0:
                #print(Node.weight-depth)
                return Node.weight - depth
            #print(val)
            val = max(val, minimax(Node.children, depth+1, alpha, beta, False, val))
            #print(val)
    else:
        val = float('inf')
        for Node in root:
            if len(Node.children) == 0:
                #print(Node.weight+depth)
                return Node.weight + depth
            val = min(val, minimax(Node.children, depth+1, alpha, beta, True, val))
            
    #print(val)
    return val

def AIAddPoint(boardArr, let):
    """
    Finds the best move for the AI and adds it to the board

    Parameters:
        boardArr (list) : List containing values (strings and integers) representing the current state of the board
        let (str) : X or O that will be placed on the boards
    
    """
    global AILet 
    global nextNode
    AILet = let
   
    initState = convertLetPos(boardArr)
    moves = moveNode(initState, 0)
    buildMoveTree([moves], AILet)
    maxWeight = float('-inf')
    nextMove = -1
    for Node in moves.children:
        weight = minimax([Node], 0, 0, 0, True, 0)
        if weight > maxWeight:
            maxWeight = weight
            nextMove = Node.state[-1]
    boardArr[nextMove] = AILet
    return boardArr

def checkWin(move):
        """
        Checks if a win condition was reached

        Parameters:
           

        Returns True if a win for the player with Tlet is detected and False if not
    
        """
        xCases = move[::2]
        oCases = move[1::2]
        for case in winCases:
                if set(case).issubset(xCases):
                    return 'X' 
                    
                elif set(case).issubset(oCases):
                    return 'O'
        return 'None'


def buildMoveTree(moves, AILet):
        """
        Build a tree containing all possible moves after the given board state and the relative win weight of each board state (-1: loss, 0: tie or no outcome, 1: win)

        Parameters:
            
            moves (list) : List containing moveNodes 
            AILet (String) : The letter for the AI ("X" or "O")

        Returns:
            moveWeights (tree) : Tree containing each possible state of the board and the associated win weight
        """
        AILet = AILet 
        if len(moves) == 0: # Returns if no child nodes were added
            return
        for Node in moves:
            currentState = Node.state # Current board state
            currentWeight = Node.weight # Win weight of sequence 
            #print(currentState, currentWeight)
            if len(currentState) == 9: # If 9 moves have been made, the game has ended
                return
            elif currentWeight != 0: # Check that sequence is not win or loss
                return
            else:
                for i in range(9):
                    if not i in currentState:
                        newMove = currentState.copy()
                        newMove.append(i) # Find possible next move
                        weight = 0
                        if len(newMove) >= 5: # A win or loss is only possible after 5 moves
                            win = checkWin(tuple(newMove))
                            if win != 'None':
                                if win == AILet:
                                    weight = winWeight # AI is maximizer
                                else:
                                    weight = -winWeight # Player is minimizer         
                        newNode = moveNode(newMove, weight)
                        Node.addChild(newNode) # Add new moveTree containing possible next move as a child of the current node

                    # If at least 5 moves have been played, check if it is a win, add 0 to children if no win or tie, -1 if loss, 1 if win
                    # If 9 moves are played, then it is a tie (0)
                    
                
            # Recursively build out the tree with possible board states
            buildMoveTree(Node.children, AILet)
            


