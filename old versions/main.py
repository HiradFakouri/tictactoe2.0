import pygame
import time

pygame.init()
back = (255,255,255)
win = pygame.display.set_mode((600,600))
pygame.display.set_caption('tic tac toe')

clock = pygame.time.Clock()

x_img = pygame.image.load('../assets/x.png')
o_img = pygame.image.load('../assets/o.png')

x_img = pygame.transform.scale(x_img, (200, 200))
o_img = pygame.transform.scale(o_img, (200, 200))

def draw_table():
    pygame.draw.line(win, (0, 0, 0), (200, 0), (200, 600), width=5)
    pygame.draw.line(win, (0, 0, 0), (400, 0), (400, 600), width=5)
    pygame.draw.line(win, (0, 0, 0), (0, 200), (600, 200), width=5)
    pygame.draw.line(win, (0, 0, 0), (0, 400), (600, 400), width=5)

turn = "x"
winner = False
draw_counter = 0
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]


def check_for_winner(board):
    global winner
    global draw_counter

    if board[0] == "x" and board[1] == "x" and board[2] == "x":
        print("x is the winner!")
        winner = True
    elif board[3] == "x" and board[4] == "x" and board[5] == "x":
        print("x is the winner!")
        winner = True
    elif board[6] == "x" and board[7] == "x" and board[8] == "x":
        print("x is the winner!")
        winner = True
    elif board[0] == "x" and board[3] == "x" and board[6] == "x":
        print("x is the winner!")
        winner = True
    elif board[1] == "x" and board[4] == "x" and board[7] == "x":
        print("x is the winner!")
        winner = True
    elif board[2] == "x" and board[5] == "x" and board[8] == "x":
        print("x is the winner!")
        winner = True
    elif board[0] == "x" and board[4] == "x" and board[8] == "x":
        print("x is the winner!")
        winner = True
    elif board[2] == "x" and board[4] == "x" and board[6] == "x":
        print("x is the winner!")
        winner = True

    if board[0] == "o" and board[1] == "o" and board[2] == "o":
        print("o is the winner!")
        winner = True
    elif board[3] == "o" and board[4] == "o" and board[5] == "o":
        print("o is the winner!")
        winner = True
    elif board[6] == "o" and board[7] == "o" and board[8] == "o":
        print("o is the winner!")
        winner = True
    elif board[0] == "o" and board[3] == "o" and board[6] == "o":
        print("o is the winner!")
        winner = True
    elif board[1] == "o" and board[4] == "o" and board[7] == "o":
        print("o is the winner!")
        winner = True
    elif board[2] == "o" and board[5] == "o" and board[8] == "o":
        print("o is the winner!")
        winner = True
    elif board[0] == "o" and board[4] == "o" and board[8] == "o":
        print("o is the winner!")
        winner = True
    elif board[2] == "o" and board[4] == "o" and board[6] == "o":
        print("o is the winner!")
        winner = True

    if draw_counter == 8 and winner == False:
        print("its a draw!")
        draw_counter = 0
        winner = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x, y = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:
        for i in range(9):
            if (
                (x > i % 3 * 200 and y > i // 3 * 200)
                and (x < (i % 3 + 1) * 200 and y < (i // 3 + 1) * 200)
                and board[i] == 0
            ):
                board[i] = turn
                turn = "o" if turn == "x" else "x"
                check_for_winner(board)
                draw_counter += 1

    win.fill(back)
    draw_table()

    for i in range(9):
        if board[i] == "x":
            win.blit(x_img, (i % 3 * 200, i // 3 * 200))
        elif board[i] == "o":
            win.blit(o_img, (i % 3 * 200, i // 3 * 200))


    pygame.display.update()
    clock.tick(60)

    if winner == True:
        time.sleep(3)
        running = False

pygame.quit()
quit()

