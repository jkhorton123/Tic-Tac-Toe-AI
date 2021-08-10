# IF X IS AI, ROOT NODE SHOULD BE SET TO MIDDLE
class Node():
    def __init__(self, state, val):
        self.weight = val
        self.state = state
        self.children = []

class moveTree():
    def __init__(self, state, val):
        self.root = Node(state, val)

    def addChild(self, child):
        self.root.children.append(child)

    
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
    for i in boardArr:
        if i == 'X':
            state.append(i)

    for j in boardArr:
        if j == 'O':
            state.append(j)
    return state

def minimax(root, alpha, beta, AIMove):
    #minimax(root.children, alpha, beta, not AIMove)
    pass

firstMove = True
def AIAddPoint(boardArr, let):
    """
    Finds the best move for the AI and adds it to the board

    Parameters:
        boardArr (list) : List containing values (strings and integers) representing the current state of the board
        let (str) : X or O that will be placed on the boards
    
    """
    global AILet 
    AILet = let
    if firstMove:
        initState = convertLetPos(boardArr)
        moves = moveTree(initState)
        buildMoveTree(moves)
    # Pass built-out moves tree with values indicating loss, tie, or win to minimax
    findBestMove = minimax(moveWeights)
    #CHANGE ABOVE LINE AND IMPLEMENT FUNCTION THAT CALLS MINIMAX AND TRAVERSES DOWN TREE EACH TIME A MOVE IS MADE BY AI OR PLAYER
    return boardArr

def checkWin(move):
        """
        Checks if a win condition was reached

        Parameters:
           

        Returns True if a win for the player with Tlet is detected and False if not
    
        """
        winCases = [(0,1,2),(0,3,6),(0,4,8),(3,4,5),(6,7,8),(1,4,7),(2,5,8),(2,4,6)]
        xCases = move[::2]
        oCases = move[1::2]
        for case in winCases:
                if set(case).issubset(xCases):
                    return 1, "X" #assumming AI is X 
                elif set(case).issubset(oCases):
                    return -1, "O"
        return 0, "None"

def buildMoveTree(moves):
        """
        Build a tree containing all possible moves after the given board state and the relative win weight of each board state (-1: loss, 0: tie or no outcome, 1: win)

        Parameters:
            
            AIMove (bool) : True if it is the AI's move and False if it is the player's

        Returns:
            moveWeights (tree) : Tree containing each possible state of the board and the associated win weight
        """
        currentMoves = moves.root.state
        if len(currentMoves[0]) != 9:
            for move in currentMoves:
                currentWeight = move.root.weight
                if currentWeight != -1 and currentWeight != 1:
                    for i in range(9):
                        if not i in move:
                            newMove = move.append(i) # Check if this mutates move
                            if len(newMove) < 5 or len(newMove) == 9:
                                weight = 0
                            else:
                                weight, win = checkWin(newMove)
                                if win != "None":
                                    if win == AILet:
                                        weight = 1
                                    else:
                                        weight = -1
                            newNode = moveTree(newMove, weight)
                            moves.addChild(newNode)

                        # If at least 5 moves have been played, check if it is a win, add 0 to children if no win or tie, -1 if loss, 1 if win
                        # If 9 moves are played, then it is a tie (0)
                
                    
        # Recursively build out the tree with possible board states
        buildMoveTree(moves.root.children)







