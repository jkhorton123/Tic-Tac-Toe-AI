winCases = [(0,1,2),(0,3,6),(0,4,8),(3,4,5),(6,7,8),(1,4,7),(2,5,8),(2,4,6)]
corners = [0, 2, 6, 8]
edges = [1, 3, 5, 7]
middle = 4
winWeight = 100000
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
        """
        self.winWeightsX = {
            # C: Corner, E: Edge, M: Middle
            #checkWin checks for win, assigning a win weight of 10000
            # 2-in-a-row for X
            'XC XE ~C': 500, 
            'XC XC ~M': 500,
            'XE XE ~M': 500,
            'XE XM ~E': 500,
            'XC XM ~C': 500,
            # AI stopping opponent win

            # corners
            'XC ~C ~E': 50,
            'XC ~C ~M': 50,
            #center
            'XM ~C ~C': 25
            }

        self.winWeightsO = {
            # C: Corner, E: Edge, M: Middle
            #checkWin checks for win, assigning a win weight of 10000
            # 2-in-a-row for X
            'OC OE ~C': 500, 
            'OC OC ~M': 500,
            'OE OE ~M': 500,
            'OE OM ~E': 500,
            'OC OM ~C': 500,
            # AI stopping opponent win

            # corners
            'OC ~C ~E': 50,
            'OC ~C ~M': 50,
            #center
            'OM ~C ~C': 25
            }
            """
        
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
"""
def convertToBoardArr(move):
    convertedBoardArr = [x for x in range(9)]
    for i in range(len(move)): 
        if i % 2 == 0:
            convertedBoardArr[move[i]] = 'X'
        else:
            convertedBoardArr[move[i]] = 'O'

    return convertedBoardArr
"""
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
    
"""

def winProbability(node):
    sumList = []
    maxIndex = -1
    maxSum = float('-inf')
    for i in range(len(node.children)):
        # For each child node, find the sum of leaves from that node and append to sumList, max is optimal move for AI
        leafSum = 0
        leafSum = addLeaves([node.children[i]], leafSum)
        sumList.append(leafSum)

        if sumList[i] > maxSum:
            maxSum = sumList[i]
            maxIndex = i
    print(sumList)
    # nextMove = node.children[maxIndex].state[-1] # Int (next space filled)
    return node.children[maxIndex] # Returns next node

def addLeaves(nodes, leafSum):
    if len(nodes) == 0:
        return 
    for Node in nodes:
        if len(Node.children) == 0:
            leafSum += Node.weight
        addLeaves(Node.children, leafSum)
    return leafSum
"""
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
    """
    if not (AILet in boardArr) : # First move for AI
        initState = convertLetPos(boardArr)
        newNode = moveNode([initState], 0)
        moves = moveNode([newNode], 0)
        buildMoveTree([moves])
    """
        #print("moves: ", moves.state)
    # Pass built-out moves tree with values indicating loss, tie, or win to minimax
    #findBestMove = minimax(moves)
   
    initState = convertLetPos(boardArr)
    #print(initState)
    moves = moveNode(initState, 0)
    buildMoveTree([moves])
    #print(moves.state[0].children[0].weight)
    maxWeight = float('-inf')
    nextMove = -1
    for Node in moves.children:
        weight = minimax([Node], 0, 0, 0, True, 0)
        #print("result: ", weight)
        if weight > maxWeight:
            maxWeight = weight
            nextMove = Node.state[-1]
    #nextNode = winProbability(nextNode)
    #CHANGE ABOVE LINE AND IMPLEMENT FUNCTION THAT CALLS MINIMAX AND TRAVERSES DOWN TREE EACH TIME A MOVE IS MADE BY AI OR PLAYER
    boardArr[nextMove] = 'X'
    return boardArr

def checkWin(move):
        """
        Checks if a win condition was reached

        Parameters:
           

        Returns True if a win for the player with Tlet is detected and False if not
    
        """
        xCases = move[::2]
        oCases = move[1::2]
        
        #print(xCases)
        #print(oCases)
        for case in winCases:
                #print(case, xCases)
                if set(case).issubset(xCases):
                    return 'X' #assumming AI is X 
                    
                elif set(case).issubset(oCases):
                    return 'O'
        return 'None'

"""
def scanMove(move, let):
  
    #Scans the 8 possible lines in the tic-tac-toe array (horizontal, vertical, and diagonals), finds the weight of each of the lines, and adds the weights to return the weight for the move
  
    weightSum = 0
    movePos = []
    boardArr = convertToBoardArr(move)

    for line in winCases:
        movePos.clear()
        for i in range(3):
            boardPos = line[i]
            Pos = boardArr[boardPos]
            # Check what letter is on the board (no letter (-), X, or O)
            if Pos != 'X' and Pos != 'O':
                movePos.append('~')
            elif Pos == 'X':
                movePos.append('X')
            else:
                movePos.append('O')

            # Check if the letter is at a corner, edge, or middle position
            if boardPos in corners:
                movePos[i] = movePos[i] + 'C'
            elif boardPos in edges: 
                movePos[i] = movePos[i] + 'E'
            elif boardPos == middle:
                movePos[i] = movePos[i] + 'M'
        
        movePos = sorted(movePos)
        lineEncoding = ' '.join(movePos)
        print(lineEncoding)
        if let == 'X':
            # Assuming AILet is X
            if lineEncoding in myAI.winWeightsX.keys():
                weightSum += myAI.winWeightsX[lineEncoding] 
            elif lineEncoding in myAI.winWeightsO.keys():
                weightSum -= myAI.winWeightsO[lineEncoding]
        else:
            # Assuming AILet is X
            if lineEncoding in myAI.winWeightsX.keys():
                weightSum -= myAI.winWeightsX[lineEncoding] 
            elif lineEncoding in myAI.winWeightsO.keys():
                weightSum += myAI.winWeightsO[lineEncoding]
    print(weightSum)
    return weightSum

"""

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
            buildMoveTree(Node.children)
            

#initNode = moveNode([6], 0)
#moves = [moveNode([initNode], 0)]
#buildMoveTree(moves)
#print(moves[0].children[6].children[2].children[0].children[3].children[0].children[2].weight)
#print(moves[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].state)
#boardArr = ['O', 'X', 'O', 'X', 4, 'X', 'X', 'O', 'O']
#boardArr = ['X', 'O', 2, 'X', 'X', 'O', 'O', 7, 8]

#print("win: ", AIAddPoint(boardArr, 'X'))

