from time import time
from Player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def printBoard(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + "| ".join(row) + "|")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for i, spot in enum(self.board):
        #     if spot == ' ':
        #         moves.append(i)
        # return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_moves(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_idx = square // 3
        row = [self.board[row_idx*3: (row_idx+1)*3]]
        if all([spot == letter for spot in row]):
            return True
        
        col_idx = square % 3
        col = [self.board[col_idx + i * 3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True

        if square % 2 == 0:
            dia1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in dia1]):
                return True
            dia2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in dia2]):
                return True
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.printBoard()
    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_moves(square, letter):
            if print_game:
                game.printBoard()
                print('')
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'
        # time.sleep(0.8)
    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    X_player = HumanPlayer('X')
    O_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, X_player, O_player, print_game=True)