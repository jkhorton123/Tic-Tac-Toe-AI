#from AIFunctions import AI


class Board():
    def __init__(self):
        self.boardArr = [x for x in range(9)]

    def checkWin(self, Tlet):
        """
        Checks if either the user or AI won

        Parameters:
            Tlet (str) : X or O

        Returns True if a win for the player with Tlet is detected and False if not
    
        """
        winCases = [(0,1,2),(0,3,6),(0,4,8),(3,4,5),(6,7,8),(1,4,7),(2,5,8),(2,4,6)]
        for case in winCases:
            if Tlet == self.boardArr[case[0]] == self.boardArr[case[1]] == self.boardArr[case[2]]:
                return True
        return False


    def printBoard(self):
        print("""
        [({0}),({1}),({2})]
        [({3}),({4}),({5})]
        [({6}),({7}),({8})]
        """.format(*self.boardArr))

    def twoPlayerUpdateBoard(self, Tlet, Ordering):
        """
        Updates the T-T-T board and displays it in the terminal

        Parameters:
            Tlet (str) : X or O that will be placed on the board
            Ordering (str) : 1st or 2nd which states which user (or AI) the letter is associated with
        

        """
        locAccepted = False
        while not locAccepted:
            if Ordering == "P1":
                loc = input("Player 1, please enter a location number: ")
                if loc.isdigit():
                    if int(loc) in range(9):
                        if str(self.boardArr[int(loc)]).isdigit():
                            self.boardArr[int(loc)] = Tlet
                            self.printBoard()
                            locAccepted = True
            
            else:
                loc = input("Player 2, please enter a location number: ")
                if loc.isdigit():
                    if int(loc) in range(9):
                        if str(self.boardArr[int(loc)]).isdigit():
                            self.boardArr[int(loc)] = Tlet
                            self.printBoard()
                            locAccepted = True



def getUserLetter():
    """
    Obtains and sets player 1's chosen letter (X or O) and the other player's (either AI or player 2)
    Note that X goes first 
    """
    
    # Set userLet to player 1's letter and otherLet to the AI's or player 2's
    letAccepted = False

    while not letAccepted:
        inputLet = input("Please enter player 1's letter (X or O): ")
        if inputLet.lower() == "x" or inputLet.lower() == "'x'":
            P1Let = 'X'
            otherLet = 'O'
            letAccepted = True

        if inputLet.lower() == "o" or inputLet.lower() == "'o'":
            P1Let = 'O'
            otherLet = 'X'
            letAccepted = True

    return P1Let, otherLet

def checkMode():
    """
    Checks and sets the user-selected mode to User Vs AI if 1 is entered and 2-player Mode if 2 is entered
    """

    modeMsg = "Enter 1 for User Vs AI Mode and Enter 2 for 2-Player Mode: "
    mode = input(modeMsg)
    while not mode.isdigit():
        mode = input(modeMsg)
    modeNum = int(mode)
    while not modeNum == 1 and not modeNum == 2:
        mode = input(modeMsg)
        modeNum = int(mode)
    return modeNum

def twoPlayerMode():
    gameBoard = Board() 
    P1Let, P2Let = getUserLetter()
    if P1Let == "X":
        first = "P1"
        second = "P2"
    else: 
        first = "P2"
        second = "P1"
    gameBoard.printBoard()

    gameEnd = False
    plays = 1
    while not gameEnd:
        if plays % 2 == 0:
            gameBoard.twoPlayerUpdateBoard('O', second)
        else:
            gameBoard.twoPlayerUpdateBoard('X', first)
            
        if plays >= 5:
            if plays % 2 == 0:
                win = gameBoard.checkWin('O')
                if win == True:
                    gameEnd = True
                    if second == "P1":
                        print("Player 1 wins!")
                    else: 
                        print("Player 2 wins!")
                    return
    
            else: 
                win = gameBoard.checkWin('X')
                if win == True:
                    gameEnd = True
                    if first == "P1":
                        print("Player 1 wins!")
                    else: 
                        print("Player 2 wins!")
                    return
        
        if plays == 9:
            gameEnd = True
            print("It's a tie!")
            return
        plays += 1

def AIMode():
    pass

def main():
    """
    Initializes and executes the game 
    """
    print("Welcome to Tic-Tac-Toe!")

    mode = checkMode()
    if mode == 1:
        AIMode()
    else: 
        twoPlayerMode()

   #userLet, AILet = getUserLetter()

    

if __name__ == "__main__":
    main()
    
