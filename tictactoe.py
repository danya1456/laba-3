class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        else:
            print("Cell already occupied! Choose another one.")
            return False

    def check_win(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.board[i][j] == self.current_player for j in range(3)) or \
               all(self.board[j][i] == self.current_player for j in range(3)):
                return True
        if all(self.board[i][i] == self.current_player for i in range(3)) or \
           all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def check_draw(self):
        return all(self.board[row][col] != ' ' for row in range(3) for col in range(3))

    def start_game(self):
        while True:
            self.print_board()
            print(f"Player {self.current_player}'s turn.")
            try:
                row, col = map(int, input("Enter row and column (0-2): ").split())
                if self.make_move(row, col):
                    if self.check_win():
                        self.print_board()
                        print(f"Player {self.current_player} wins!")
                        break
                    elif self.check_draw():
                        self.print_board()
                        print("It's a draw!")
                        break
                    self.current_player = 'O' if self.current_player == 'X' else 'X'
            except (ValueError, IndexError):
                print("Invalid input. Enter row and column as numbers between 0 and 2.")
