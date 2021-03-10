import pygame
from pygame.locals import *
import numpy as np

DEAD = '.'
ALIVE = '*'
BOARD_SIZE = 500

# List of coordinates where cells are alive on initialization
INITIAL_STATE = [
    (1,1),
    (1,2),
    (2,1),
    (3,1)
]

class Cell:
    def __init__(self, state=DEAD):
        self.state = state

class View:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Game of Life')
        self.window = pygame.display.set_mode((BOARD_SIZE,BOARD_SIZE))
        self.background = pygame.Surface( self.window.get_size() )
        self.background.fill( (0,0,0) )
        self.window.blit( self.background, (0,0) )
        pygame.display.flip()

class GameOfLife:
    def __init__(self, initial_state, size=10):
        self.board = np.full((size,size), DEAD)
        for pos in initial_state:
            self.board[pos[0],pos[1]] = Cell(ALIVE)

    def tick(self):
        return

if __name__ == "__main__":
    game = GameOfLife(INITIAL_STATE)
    view = View()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            else:
                game.tick()
