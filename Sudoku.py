
class Sodoku():
    my_Board = [
        [0,0,0,3,9,0,0,1,0],
        [5,0,1,0,0,0,0,4,0],
        [9,0,0,7,0,0,5,0,0],
        [6,0,2,5,3,0,0,7,0],
        [0,0,0,0,7,0,0,0,8],
        [7,0,0,8,0,0,9,0,3],
        [8,0,3,0,1,0,0,9,0],
        [0,9,0,2,0,6,0,0,7],
        [4,0,0,0,0,3,0,6,1]
    ]
    
    solutions = [
        [2,4,8,3,9,5,7,1,6],
        [5,7,1,6,2,8,3,4,9],
        [9,3,6,7,4,1,5,8,2],
        [6,8,2,5,3,9,1,7,4],
        [3,5,9,1,7,4,6,2,8],
        [7,1,4,8,6,2,9,5,3],
        [8,6,3,4,1,7,2,9,5],
        [1,9,5,2,8,6,4,3,7],
        [4,2,7,9,5,3,8,6,1]
    ]

    def get_Board(self):
        return self.my_Board

    def get_Solutions(self):
        return self.solutions
    
    def set_Board(self, x, y, v):
        self.my_Board[x][y] = v

    def print_Board(self):
        b = self.get_Board()

        for i in range(0,9):
            print("[", end = "")
            for j in range(0,9):
                if(j == 8):
                    print(b[i][j], end = "")
                else:
                    print(b[i][j], end = ",")

            print("]")


def main():
    game = Sodoku()
    game.print_Board()
    solutions = game.get_Solutions()
    game_board = game.get_Board()

    while(True):
        x_Val = int(input("\nEnter X position: "))
        y_Val = int(input("Enter Y position: "))

        if(game_board[x_Val][y_Val] != 0):
            print("Error: Cannot Enter Value Here")
            continue

        num   = int(input("Enter Number To Enter: "))
        if(solutions[x_Val][y_Val] == num):
            print("\nCorrect!")
            game.set_Board(x_Val, y_Val, num)
            game.print_Board()
        else:
            print("Wrong! Try Again..")

if __name__ == "__main__":
    main()