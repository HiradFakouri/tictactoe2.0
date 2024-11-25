#still in progree not used in the main game yet.
#this will make the dum ai into a smart one :)
score = {
    "o": 10,
    "x": -10
}

def isGameOver(board):
    for i in range(9):
        if board[i] == 0:
            return True

    return False

def gameStatus(board):
    avalibleMoves = []

    if isGameOver(board):
        for i in range(9):
            if board[i] == 0:
                avalibleMoves.append(i)

    return avalibleMoves

def scoreF(board):

    if check_for_winner(board) == "o":
        return score["o"]
    elif check_for_winner(board) == "x":
        return score["x"]
    else:
        return 0

def minmax(board):
    if check_for_winner(board) != False:
        return scoreF(board)

    scores = []
    moves = []

    for move in board:
        possible_game = gameStatus(board)
        scores.append(minmax(possible_game))