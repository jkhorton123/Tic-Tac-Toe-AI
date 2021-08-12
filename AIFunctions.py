# IF X IS AI, ROOT NODE SHOULD BE SET TO MIDDLE
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
        moves = moveNode(initState)
        buildMoveTree(moves)
    # Pass built-out moves tree with values indicating loss, tie, or win to minimax
    findBestMove = minimax(moves)
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
            
            moves (list) : List containing moveNodes 

        Returns:
            moveWeights (tree) : Tree containing each possible state of the board and the associated win weight
        """
        AILet = 'X' # DELETE THIS LATER
        if len(moves) == 0: # Returns if no child nodes were added
            return
        for Node in moves:
            currentState = Node.state # Current board state
            currentWeight = Node.weight # Win weight of sequence 
            if len(currentState) == 9: # If 9 moves have been made, the game has ended
                continue
            elif currentWeight != 0: # Check that sequence is not win or loss
                continue
            else:
                for i in range(9):
                    if not i in currentState:
                        newMove = currentState.copy()
                        newMove.append(i) # Find possible next move
                        if len(newMove) < 5: # A win or loss is only possible after 5 moves
                            weight = 0
                        else:
                            weight, win = checkWin(newMove)
                            #print(win, weight)
                            if win != "None":
                                if win == AILet:
                                    weight = 1 # AI is maximizer
                                else:
                                    weight = -1 # Player is minimizer
                        newNode = moveNode(newMove, weight)
                        Node.addChild(newNode) # Add new moveTree containing possible next move as a child of the current node

                    # If at least 5 moves have been played, check if it is a win, add 0 to children if no win or tie, -1 if loss, 1 if win
                    # If 9 moves are played, then it is a tie (0)
                    
                
            # Recursively build out the tree with possible board states
            buildMoveTree(Node.children)

moves = [moveNode([6], 0)]
buildMoveTree(moves)
#print(moves[0].children[6].children[2].children[0].children[3].children[0].children[0].children[0].weight)
#print(moves[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].state)