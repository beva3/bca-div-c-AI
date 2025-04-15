# this game is just easy to learn OPP
# and it is a good example of how to use OOP in python

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        
    
    def print_board(self):
        print()
        print("Current board:")
        for i in range(3):
            print(f"{self.board[i*3]} | {self.board[i*3 + 1]} | {self.board[i*3 + 2]}")
            if i < 2:
                print("---------")
        print()
    
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        
    
                
    
    def play(self):
        while True:
            self.print_board()
            try :
                position = int(input(f"Player {self.current_player}, enter your move (1-9): ")) - 1

            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            
            self.switch_player()
            
game = TicTacToe()
game.play()
        
        