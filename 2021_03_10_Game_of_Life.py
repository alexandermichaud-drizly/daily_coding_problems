import pygame
from pygame.locals import *
import numpy as np

DEAD = 0
ALIVE = 1
SIZE = 50
BOARD_PIXELS = 500
CELL_SIZE = BOARD_PIXELS / SIZE

# List of coordinates where cells are alive on initialization
INITIAL_STATE = [
    (1,1),
    (1,2),
    (2,1),
    (3,1)
]

class Cell:
    def __init__(self):
        self.state = DEAD

    def is_alive(self):
        return self.state == ALIVE 

    def live(self):
        self.state = ALIVE

    def die(self):
        self.state = DEAD

class View:
    def __init__(self, game):
        self.game = game
        pygame.init()
        pygame.display.set_caption('Game of Life')
        self.window = pygame.display.set_mode((BOARD_PIXELS,BOARD_PIXELS))
        self.background = pygame.Surface( self.window.get_size() )
        self.background.fill( (0,0,0) )
        self.draw_board()

    def draw_board(self):
        self.window.blit( self.background, (0,0) )

        for x, row in enumerate(self.game.board):
            for y, cell in enumerate(row):
                if cell.is_alive():
                    live_cell = pygame.Surface( (CELL_SIZE,CELL_SIZE) )
                    live_cell.fill((255,255,255))
                    self.window.blit(live_cell, (x * CELL_SIZE, y * CELL_SIZE))
                    
        pygame.display.flip()

class GameOfLife:
    def __init__(self, initial_state=INITIAL_STATE, size=SIZE):
        self.board = np.ndarray((SIZE,SIZE), dtype=np.object)
        for x, row in enumerate(self.board):
            for y, cell in enumerate(row):
                self.board[x,y] = Cell()

        for pos in initial_state:
            cell = self.board[pos[0],pos[1]]
            cell.live()

    def tick(self):
        # prev_board = self.
        return

if __name__ == "__main__":
    game = GameOfLife()
    view = View(game)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            else:
                game.tick()
                view.draw_board()
