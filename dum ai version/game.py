import pygame
import time
import logic
import random

class Game:

    def __init__(self):
        self.back = (255, 255, 255)
        self.win = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('tic tac toe')

        self.clock = pygame.time.Clock()

        x_img = pygame.image.load('assets/x.jpg')
        o_img = pygame.image.load('assets/o.jpg')
        table = pygame.image.load('assets/board.jpg')

        self.x_img = pygame.transform.scale(x_img, (180, 180))
        self.o_img = pygame.transform.scale(o_img, (180, 180))
        self.table = pygame.transform.scale(table, (600, 600))

        self.turn = "x"
        self.winner = False
        self.draw_counter = 0
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def main(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            x, y = pygame.mouse.get_pos()

            if self.turn == "x":
                if pygame.mouse.get_pressed()[0]:
                    for i in range(9):
                        if (
                                (x > i % 3 * 200 and y > i // 3 * 200)
                                and (x < (i % 3 + 1) * 200 and y < (i // 3 + 1) * 200)
                                and self.board[i] == 0
                        ):
                            if self.turn == "x":
                                self.board[i] = self.turn
                                self.turn = "o" if self.turn == "x" else "x"

                                self.winner = logic.check_for_winner(self.board)


            else:
                placement = random.randint(0, 8)
                while self.board[placement] != 0:
                    placement = random.randint(0, 8)

                self.board[placement] = self.turn
                self.turn = "x" if self.turn == "o" else "o"

                self.winner = logic.check_for_winner(self.board)



            self.win.fill(self.back)
            logic.draw_table(self.win)

            for i in range(9):
                if self.board[i] == "x":
                    self.win.blit(self.x_img, (i % 3 * 210, i // 3 * 210))
                elif self.board[i] == "o":
                    self.win.blit(self.o_img, (i % 3 * 210, i // 3 * 210))

            pygame.display.update()
            self.clock.tick(60)

            if self.winner == "x":
                print("x is the winner!")
                time.sleep(3)
                running = False
            elif self.winner == "o":
                print("o is the winner!")
                time.sleep(3)
                running = False
            elif self.winner:
                print("its a Draw!")
                time.sleep(3)
                running = False
            else:
                continue

        pygame.quit()
        quit()
