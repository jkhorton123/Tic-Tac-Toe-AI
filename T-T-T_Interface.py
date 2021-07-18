boardArr = [x+1 for x in range(9)]
class Board():
    
    def updateBoard(self, Tloc, Tlet):
        """
        Updates the T-T-T board and displays it in the terminal

        Parameters 
        ----------
        Tloc = int
            Location of X or O on the board
        Tlet = str
            X or O that will be placed on the board
        """
        global boardArr
        boardArr[Tloc] = Tlet
        print("""
        [({0}),({1}),({2})]
        [({3}),({4}),({5})]
        [({6}),({7}),({8})]
        """.format(*boardArr))

def main():
    """
    Initializes and executes the game 
    """
    print("Welcome to Tic-Tac-Toe!")
    p1Let = input("Please enter your chosen letter (X or O): ")
    print(p1Let)



if __name__ == "__main__":
    main()
    
