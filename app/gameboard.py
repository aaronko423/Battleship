#! usr/bin/env python3

BLANK = '   '
SHIP  = 'S'
MISS  = 'M'
HIT   = 'X'

import random

class GameBoard:
    
    x_ran = random.randint(0,4)
    y_ran = random.randint(0,4)

    def __init__(self, width=4, height=4):
        grid = []
        print("")
        for row_index in range(height):
            new_row = []
            for col_index in range(width):
                new_row.append(BLANK)
            grid.append(new_row)
            print(new_row)
        self.grid = grid
        print(self.x_ran, self.y_ran)
        
    def input(self, x_input, y_input):
        if x_input == self.x_ran and y_input == self.y_ran:
            self.grid[x_input][y_input] = ["X"]
        else:
            self.grid[x_input][y_input] = ["M"]
        self.print()

    def print(self):
        print("")
        for row_index in self.grid:
            print(row_index)
        print("")
        

if __name__=='__main__':
   g = GameBoard()
   g.input(0,0)
