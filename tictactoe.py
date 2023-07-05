import pygame
from enum import Enum

pygame.init()
font = pygame.font.Font('arial.ttf', 75)


class Player(Enum):
    P1 = 0
    P2 = 1
    TIE = 2


# pygame constants
BLOCK_SIZE = 80

# rgb colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)


class TTTGame:
    def __init__(self, board_size=5):
        # Pygame display
        self.board_size = board_size
        self.w = BLOCK_SIZE * self.board_size
        self.h = BLOCK_SIZE * self.board_size
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Tic Tac Toe')

        self.turn = None
        self.board = None
        self.reset()

    def reset(self):
        self.turn = False
        self.board = [[None for i in range(self.board_size)] for j in range(self.board_size)]
        self.draw_ui()

    def is_winner(self):
        for i in range(2, len(self.board)):
            for j in range(len(self.board)):
                # Detect Horizontal
                if self.board[i][j] == self.turn and \
                        self.board[i - 1][j] == self.turn and \
                        self.board[i - 2][j] == self.turn:
                    return True
                # Detect Vertical
                if self.board[j][i] == self.turn and \
                        self.board[j][i - 1] == self.turn and \
                        self.board[j][i - 2] == self.turn:
                    return True
                # Detect Diagonals
                # \
                if j >= 2 and self.board[i][j] == self.turn and \
                        self.board[i - 1][j - 1] == self.turn and \
                        self.board[i - 2][j - 2] == self.turn:
                    return True
                # /
                if j < len(self.board) - 2 and \
                        self.board[i][j] == self.turn and \
                        self.board[i - 1][j + 1] == self.turn and \
                        self.board[i - 2][j + 2] == self.turn:
                    return True

        return False

    def is_tie(self):
        for i in range(len(self.board)):
            if None in self.board[i]:
                return False

        return True

    def play_step(self):
        # 1: collect user input
        result = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[0] // BLOCK_SIZE, pos[1] // BLOCK_SIZE
                # 1.5: Check if valid move
                if self.board[row][col] is None:
                    self.board[row][col] = self.turn
                else:
                    print('That is not a legal move!')
                    break

                # 2: Check for winner or tie
                if self.is_winner():
                    result = self.turn
                if self.is_tie():
                    result = 2

                self.turn = not self.turn

                # 3: Draw Board
                self.draw_ui()
        return result

    def draw_ui(self):
        self.display.fill(BLACK)
        for i in range(0, self.board_size):
            for j in range(0, self.board_size):
                rect = pygame.Rect(i * BLOCK_SIZE, j * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(self.display, WHITE, rect, 1)

                if self.board[i][j] is False:
                    self.display.blit(font.render('O', False, BLUE), ((i + 0.1) * BLOCK_SIZE, j * BLOCK_SIZE))
                elif self.board[i][j] is True:
                    self.display.blit(font.render('X', False, RED), ((i + 0.1) * BLOCK_SIZE, j * BLOCK_SIZE))

        pygame.display.flip()


if __name__ == '__main__':
    # create game
    while True:
        num = input('Enter game size [1-10]: ')
        if num.isdigit() and 0 <= int(num) <= 10:
            break
        else:
            print("Please input an integer between 1-10!")
    game = TTTGame(int(num))

    # game loop
    while True:
        winner = game.play_step()

        if winner is not None:
            print('Winner:', Player(winner).name)
            pygame.time.delay(1000)
            game.reset()
