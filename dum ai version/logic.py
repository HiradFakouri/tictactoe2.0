import pygame


def check_for_winner(board):
    if board[0] == "x" and board[1] == "x" and board[2] == "x":
        return "x"
    elif board[3] == "x" and board[4] == "x" and board[5] == "x":
        return "x"
    elif board[6] == "x" and board[7] == "x" and board[8] == "x":
        return "x"
    elif board[0] == "x" and board[3] == "x" and board[6] == "x":
        return "x"
    elif board[1] == "x" and board[4] == "x" and board[7] == "x":
        return "x"
    elif board[2] == "x" and board[5] == "x" and board[8] == "x":
        return "x"
    elif board[0] == "x" and board[4] == "x" and board[8] == "x":
        return "x"
    elif board[2] == "x" and board[4] == "x" and board[6] == "x":
        return "x"

    if board[0] == "o" and board[1] == "o" and board[2] == "o":
        return "o"
    elif board[3] == "o" and board[4] == "o" and board[5] == "o":
        return "o"
    elif board[6] == "o" and board[7] == "o" and board[8] == "o":
        return "o"
    elif board[0] == "o" and board[3] == "o" and board[6] == "o":
        return "o"
    elif board[1] == "o" and board[4] == "o" and board[7] == "o":
        return "o"
    elif board[2] == "o" and board[5] == "o" and board[8] == "o":
        return "o"
    elif board[0] == "o" and board[4] == "o" and board[8] == "o":
        return "o"
    elif board[2] == "o" and board[4] == "o" and board[6] == "o":
        return "o"

    counter = 1

    for i in range(9):
        if board[i] != 0:
            counter += 1

    if counter == 10:
        return True

    return False



def draw_table(win):
    pygame.draw.line(win, (0, 0, 0), (200, 0), (200, 600), width=5)
    pygame.draw.line(win, (0, 0, 0), (400, 0), (400, 600), width=5)
    pygame.draw.line(win, (0, 0, 0), (0, 200), (600, 200), width=5)
    pygame.draw.line(win, (0, 0, 0), (0, 400), (600, 400), width=5)



