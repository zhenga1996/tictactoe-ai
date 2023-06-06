import pygame
from enum import Enum

pygame.init()
font = pygame.font.Font('arial.ttf', 150)

# pygame constants
BLOCK_SIZE = 160

# rgb colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)


class TTTGame:
    def __init__(self, w=BLOCK_SIZE * 3, h=BLOCK_SIZE * 3):
        # Pygame display
        self.w = w
        self.h = h
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Tic Tac Toe')

        self.turn = None
        self.board = None
        self.reset()

    def reset(self):
        self.turn = False
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

    def play_step(self):
        # 1. collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for i in range(3):
                    for j in range(3):
                        if i * BLOCK_SIZE <= mouse_x < (i + 1) * BLOCK_SIZE and j * BLOCK_SIZE <= mouse_y < (
                                j + 1) * BLOCK_SIZE:
                            self.board[i][j] = self.turn
                            self.turn = not self.turn

        # TODO: check if game over
        game_over = False

        self.draw_ui()

        return game_over

    def draw_ui(self):
        self.display.fill(BLACK)
        for i in range(0, 3):
            for j in range(0, 3):
                rect = pygame.Rect(i * BLOCK_SIZE, j * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(self.display, WHITE, rect, 1)

                if self.board[i][j] == 0:
                    self.display.blit(font.render('O', False, BLUE), ((i+0.15)*BLOCK_SIZE, j*BLOCK_SIZE))
                elif self.board[i][j] == 1:
                    self.display.blit(font.render('X', False, RED), ((i+0.15)*BLOCK_SIZE, j*BLOCK_SIZE))

        pygame.display.flip()


if __name__ == '__main__':
    game = TTTGame()

    # game loop
    while True:
        game_over = game.play_step()

        if game_over:
            break

    print('Winner: ')

    pygame.quit()
