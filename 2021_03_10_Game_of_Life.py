import pygame
from pygame.locals import *
import numpy as np
import copy, time, sys, getopt

DEAD = 0
ALIVE = 1
SIZE = 50 
BOARD_PIXELS = 500
CELL_SIZE = BOARD_PIXELS / SIZE

# Initializers 
TOAD = [
    (10,10),
    (10,11),
    (10,12),
    (9, 10),
    (9, 11),
    (9, 9)
]

GLIDER = [
    (10,10),
    (10,11),
    (10,12),
    (9,12),
    (8,11)
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
    def __init__(self, initial_state, size=SIZE):
        self.board = np.ndarray((SIZE,SIZE), dtype=np.object)
        for x, row in enumerate(self.board):
            for y, cell in enumerate(row):
                self.board[x,y] = Cell()

        for pos in initial_state:
            cell = self.board[pos[0],pos[1]].live()

    def tick(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return False

        prev_board = copy.deepcopy(self.board)
        for x, row in enumerate(prev_board):
            for y, cell in enumerate(row):
                live_neighbors = 0

                if x > 0:
                    live_neighbors += prev_board[x - 1, y].is_alive()
                if x < SIZE - 1:
                    live_neighbors += prev_board[x + 1, y].is_alive()
                if y > 0:
                    live_neighbors += prev_board[x, y - 1].is_alive()
                if y < SIZE - 1:
                    live_neighbors += prev_board[x, y + 1].is_alive()
                if x > 0 and y > 0:
                    live_neighbors += prev_board[x - 1, y - 1].is_alive()
                if x < SIZE - 1 and y > 0:
                    live_neighbors += prev_board[x + 1, y - 1].is_alive()
                if x > 0 and y < SIZE - 1:
                    live_neighbors += prev_board[x - 1, y + 1].is_alive()
                if x < SIZE - 1 and y < SIZE - 1:
                    live_neighbors += prev_board[x + 1, y + 1].is_alive()
                
                if cell.is_alive(): 
                    if live_neighbors < 2 or live_neighbors > 3:
                        self.board[x,y].die()
                elif live_neighbors == 3:
                    self.board[x,y].live()

        return True

if __name__ == "__main__":
    args = sys.argv[1:]
    try:
        opts, args = getopt.getopt(args,"i:",["initialize="])
    except getopt.GetoptError:
        print('Invalid arguments')
        sys.exit(2)

    initial_state = None
    for opt, arg in opts:
        if opt in ("-i", "--initialize"):
            if arg == 'toad':
                initial_state = TOAD
            elif arg == 'glider':
                initial_state = GLIDER

    if initial_state is None:
        print('No initial pattern provided')
        sys.exit()

    game = GameOfLife(initial_state)
    view = View(game)
    running = True
    while running:
        running = game.tick()
        view.draw_board()
        time.sleep(0.1)
