
class Board():
    def __init__(self):
        self.boardArr = [x for x in range(9)]

    def checkWin(self, Tlet):
        """
        Checks if either the user or AI won

        Parameters:
            Tlet (str) : X or O

        Returns the winning letter if a win is detected and "False" if not
    
        """
        winCases = [(0,1,2),(0,3,6),(0,4,8),(3,4,5),(6,7,8),(1,4,7),(2,5,8),(2,4,6)]
        for case in winCases:
            if self.boardArr[case[0]] == self.boardArr[case[1]] == self.boardArr[case[2]]:
                return self.boardArr[case[0]]
        return "False"


    def printBoard(self):
        print("""
        [({0}),({1}),({2})]
        [({3}),({4}),({5})]
        [({6}),({7}),({8})]
        """.format(*self.boardArr))

    def updateBoard(self, Tlet):
        """
        Updates the T-T-T board and displays it in the terminal

        Parameters 
        ----------
        Tlet = str
            X or O that will be placed on the board
        """
        locAccepted = False
        while not locAccepted:
            loc = input("Enter a location number: ")
            if loc.isdigit():
                if int(loc) in range(9):
                    if str(self.boardArr[int(loc)]).isdigit():
                        self.boardArr[int(loc)] = Tlet
                        self.printBoard()
                        locAccepted = True


def getUserLetter():
    """
    Obtains and sets the user's chosen letter (X or O) and the AI's
    """
    
    # Set userLet to the user's letter and AILet to the AI's
    letAccepted = False

    while not letAccepted:
        inputLet = input("Please enter your chosen letter (X or O): ")
        if inputLet.lower() == "x" or inputLet.lower() == "'x'":
            userLet = "X" 
            AILet = "O"
            letAccepted = True

        if inputLet.lower() == "o" or inputLet.lower() == "'o'":
            userLet = "O"
            AILet = "X"
            letAccepted = True

    return userLet, AILet

def main():
    """
    Initializes and executes the game 
    """
    gameBoard = Board() 
    print("Welcome to Tic-Tac-Toe!")
    userLet, AILet = getUserLetter()

    gameBoard.printBoard()

    gameEnd = False
    plays = 1
    while not gameEnd:
        if plays % 2 == 0:
            gameBoard.updateBoard(AILet)
        else:
            gameBoard.updateBoard(userLet)
            
        if plays >= 5:
            win = gameBoard.checkWin(userLet)
            if win == userLet:
                gameEnd = True
                print("User wins!")
                return
            if win == AILet:
                gameEnd = True
                print("AI wins!")
                return
        if plays == 9:
            gameEnd = True
            print("It's a tie!")
        plays += 1

if __name__ == "__main__":
    main()
    
