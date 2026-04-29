def new_board():
    return [None] * 9 

def print_board(board):
    symbols = {None: '.', 'X': 'X', '0': '0'}
    for row in range(3):
        cells = board[row*3 : row*3 + 3]
        print(' | '.join(symbols[c] for c in cells))
    print()

if __name__ == "__main__":
    board = new_board()
    board[4] = 'X'
    print_board(board)