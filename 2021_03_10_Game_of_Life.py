import pygame
from pygame.locals import *
import numpy as np
import copy

DEAD = 0
ALIVE = 1
SIZE = 50
BOARD_PIXELS = 500
CELL_SIZE = BOARD_PIXELS / SIZE

# List of coordinates where cells are alive on initialization
INITIAL_STATE = [
    (10,10),
    (10,11),
    (10,12)
]

class Cell:
    def __init__(self):
        self.state = DEAD
        self.neighbors = []

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

        for x, row in enumerate(self.board):
            for y, cell in enumerate(row):
                neighbors = []

                if x > 0:
                    neighbors.append(self.board[x - 1, y])
                if x < SIZE - 1:
                    neighbors.append(self.board[x + 1, y])
                if y > 0:
                    neighbors.append(self.board[x, y - 1])
                if y < SIZE - 1:
                    neighbors.append(self.board[x, y + 1])
                if x > 0 and y > 0:
                    neighbors.append(self.board[x - 1, y - 1])
                if x < SIZE - 1 and y > 0:
                    neighbors.append(self.board[x + 1, y - 1])
                if x > 0 and y < SIZE - 1:
                    neighbors.append(self.board[x - 1, y + 1])
                if x < SIZE - 1 and y < SIZE - 1:
                    neighbors.append(self.board[x + 1, y + 1])

                self.board[x,y].neighbors = neighbors
       

        for pos in initial_state:
            cell = self.board[pos[0],pos[1]].live()

    def tick(self):
        prev_board = copy.deepcopy(self.board)
        for x, row in enumerate(prev_board):
            for y, cell in enumerate(row):
                live_neighbors = 0
                for neighbor in cell.neighbors:
                    if neighbor.is_alive():
                        live_neighbors += 1
                
                if cell.is_alive(): 
                    if live_neighbors < 2 or live_neighbors > 3:
                        print(x,y)
                        self.board[x,y].die()
                elif live_neighbors == 3:
                    self.board[x,y].live()

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
