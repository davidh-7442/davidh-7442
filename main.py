import string
import sys

possiblePieces = {'wking': 1, 'wqueen': 1, 'wrook': 2, 'wknight': 2, 'wbishop': 2, 'wpawn': 8, 'bking': 1, 'bqueen': 1,
                  'brook': 1, 'bknight': 2, 'bbishop': 2, 'bpawn': 8}

chessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '1a': 'bbishop',
              '3g': 'wpawn',
              '3f': 'wpawn'}

count = {}


def pieceValidation(board):
    # this counts the amount of pieces on the board
    for piece in board.values():
        count.setdefault(piece, 0)
        count[piece] = count[piece] + 1

    # this checks if there is a valid number of pieces on the board
    for piece in count:
        # checks whether there are a valid number of kings on the board
        if 'king' in piece:
            if count.get(piece) != 1:
                print('There is an invalid number of kings')
                sys.exit()

        # this handles every other piece checking if theres a valid number of pieces, ie 8 white pawns
        elif count.get(piece) > possiblePieces.get(piece):
            print('Invalid number of ' + piece + 's.')
            sys.exit()


# checks for valid board
def boardValidation(board):

    letters = string.ascii_lowercase[0:8] # gets letters a-h
    boardPositions = []

    # creates a list of board positions
    for letter in letters:
        for i in range(0, 8):
            current = str(i + 1) + letter
            boardPositions.append(current)

    # checks to see if the positions of the entered board are valid against boardPositions
    for position in board:
        if position not in boardPositions:
            print('There is a piece in an invalid position: ' + position)


# defines main
def main():
    pieceValidation(chessBoard)
    boardValidation(chessBoard)


# runs main()
if __name__ == '__main__':
    main()