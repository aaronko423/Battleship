#! usr/bin/env python3

import os

BLANK = '   '
SHIP  = 'S'
MISS  = 'M'
HIT   = 'X'

class GameBoard:
    
    def __init__(self, width=10, height=10):
        self.grid1 = []
        self.grid2 = []
        
        for row_index in range(height):
            new_row= []
            for col_index in range(width):
                new_row.append(BLANK)
            self.grid1.append(new_row)
            
        for row_index2 in range(height):
            new_row2= []
            for col_index2 in range(width):
                new_row2.append(BLANK)
            self.grid2.append(new_row2)   
        
    def input_by_player1(self, player1_guess_x, player1_guess_y, player2_set_x, player2_set_y):
        
        if player1_guess_x == player2_set_x and player1_guess_y == player2_set_y:
            self.grid2[player1_guess_x-1][player1_guess_y-1] = ["X"]
        else:
            self.grid2[player1_guess_x-1][player1_guess_y-1] = ["M"]

        self.print_player2_grid()

    def input_by_player2(self, player2_guess_x, player2_guess_y, player1_set_x, player1_set_y):

        if player2_guess_x == player1_set_x and player2_guess_y == player1_set_y:
            self.grid1[player2_guess_x-1][player2_guess_y-1] = ["X"]
        else:
            self.grid1[player2_guess_x-1][player2_guess_y-1] = ["M"]

        self.print_player1_grid()

    def print_player1_grid(self):
        print("")
        for row_index in self.grid1:
            print(row_index)
        print("")

    def print_player2_grid(self):
        print("")
        for row_index in self.grid2:
            print(row_index)
        print("")
        

if __name__=='__main__':
   g = GameBoard()
   g.input(0,0)
