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
        
    
    def make_position(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
        else:
            print("Position already taken. Try again.")
            return False
        return True
    
    def check_draw(self):
        return ' ' not in self.board
    
    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # columns
            (0, 4, 8), (2, 4, 6)             # diagonals
        ]
        
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False
                
    
    def play(self):
        while True:
            self.print_board()
            try :
                position = int(input(f"Player {self.current_player}, enter your move (1-9): ")) - 1
                
                if not self.make_position(position):
                    continue
                
                if self.check_draw():
                    self.print_board()
                    print("It's a draw!")
                    break
                
                if self.check_winner():
                    self.print_board()
                    print(f"Player {self.current_player} wins!")
                    break
                
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            
            self.switch_player()
            
game = TicTacToe()
game.play()
        
        