# IF X IS AI, ROOT NODE SHOULD BE SET TO MIDDLE
class Node():
    def __init__(self, val):
        self.data = val
        self.children = []

class moveTree():
    def __init__(self, val):
        self.root = Node(val)

    def addChild(self, root, val):
        root.children.append(val)

class AI(object):
    def __init__(self, val):
        self.root = Node(val)

    
    """
    def posWeights(self):
        
        #Initializes dictionaries containing the weights of each subsequent possible move for the AI
        
        XDict = {
        'XXX': 1000000, # Win
        'OOX': 10000, # Stop user from winning
        '0XX': 100, 
        'XX8': 100,
        '2XX': 100,
        'XX6': 100,
        ' XX': 100 ,
        }
    """


def AIAddPoint(boardArr, let, numMoves):
    """
    Finds the best move for the AI and adds it to the board

    Parameters:
        boardArr (list) : List containing values determining the current state of the board
        let (str) : X or O that will be placed on the board
        numMoves (int) : Number of total moves made so far
    
    """
    moveWeights = buildMoveTree(boardArr)
    findBestMove = minimax(moveWeights)
    return boardArr

"""
def buildMoveTree(boardArr):

    moveWeights = moveTree()
    for i in boardArr:
        if not i == 'X' and not i == 'O':
            boardArrChild = 
    buildMoveTree(boardArr)
    return moveWeights

"""

def minimax(root, alpha, beta, maxTurn):
    pass




