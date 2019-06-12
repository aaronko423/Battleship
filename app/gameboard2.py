#! usr/bin/env python3

BLANK = '   '
SHIP  = 'S'
MISS  = 'M'
HIT   = 'X'

import random

class GameBoard:
    
    x_ran1 = random.randint(0,4)
    y_ran1 = random.randint(0,4)

    x_ran2 = random.randint(0,4)
    y_ran2 = random.randint(0,4)

    def __init__(self, width=5, height=5):
        grid1 = []
        grid2 = []
        print("")
        for row_index in range(height):
            for col_index in range(width):
                new_row.append(BLANK)
            grid1.append(new_row)
            grid2.append(new_row)
            print(new_row)
        self.grid1 = grid1
        self.grid2 = grid2
        
    def input_in_player1(self, x_input1, y_input1):
        
        print(self.x_ran1, self.y_ran1)
        
        if x_input1 == self.x_ran1 and y_input1 == self.y_ran1:
            self.grid1[x_input1][y_input1] = ["X"]
        else:
            self.grid1[x_input1][y_input1] = ["M"]
        self.print_player1()

    def input_in_player2(self, x_input2, y_input2):

        print(self.x_ran2, self.y_ran2)

        if x_input2 == self.x_ran2 and y_input2 == self.y_ran2:
            self.grid2[x_input2][y_input2] = ["X"]
        else:
            self.grid2[x_input2][y_input2] = ["M"]
        self.print_player2()
        
    def print_player1(self):
        print("")
        for row_index in self.grid1:
            print(row_index)
        print("")

    def print_player2(self):
        print("")
        for row_index in self.grid2:
            print(row_index)
        print("")
        

if __name__=='__main__':
   g = GameBoard()
   g.input(0,0)
