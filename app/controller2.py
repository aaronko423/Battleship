#! usr/bin/env python3

from gameboard2 import GameBoard
import os

g = GameBoard()

def user_gameplay():
    
    print("\nWelcome to battleship!\n")
    player1_name = input("Player 1, please enter your name: \n")
    player2_name = input("Player 2, please enter your name: \n")

    os.system("clear")

    g.print_player1_grid()
    player1_set_x = int(input(f"{player1_name}, please set your x value [1-10] for the battleship: "))
    player1_set_y = int(input(f"{player1_name}, please set your y value [1-10] for the battleship: "))

    os.system("clear")

    g.print_player2_grid()
    player2_set_x = int(input(f"{player2_name}, please set your x value [1-10] for the battleship: "))
    player2_set_y = int(input(f"{player2_name}, please set your y value for [1-10] the battleship: "))
    
    os.system("clear")
    
    player1_guess_x = None
    player1_guess_y = None
    player2_guess_x = None
    player2_guess_y = None
    
    acceptable_inputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    while True:
        
        print(f"\nMake your battleship attack, {player1_name}!\n")

        while player1_guess_x not in acceptable_inputs:
            player1_guess_x = input(f"{player1_name}, enter an x coordinate for where you think {player2_name}'s ship is: ")
            if player1_guess_x not in acceptable_inputs:
                print('Please enter a digit between 1 and 10!')    
        
        while player1_guess_y not in acceptable_inputs:
            player1_guess_y = input(f"{player1_name}, enter a y coordinate for where you think {player2_name}'s ship is: ")
            if player1_guess_y not in acceptable_inputs:        
                print('Please enter a digit between 1 and 10!')

        os.system("clear")

        player1_guess_x = int(player1_guess_x)
        player1_guess_y = int(player1_guess_y)
        g.input_by_player1(player1_guess_x, player1_guess_y, player2_set_x, player2_set_y)

        if player1_guess_x == player2_set_x and player1_guess_y == player2_set_y:
            print(f"{player1_name}, you are the winner!")
            break
        
        print(f"\nMake your battleship attack, {player2_name}!\n")
        
        while player2_guess_x not in acceptable_inputs:
            player2_guess_x = input(f"{player2_name}, enter an x coordinate for where you think {player1_name}'s ship is: ")
            if player2_guess_x not in acceptable_inputs:
                print('Please enter a digit between 1 and 10!')    
        
        while player2_guess_y not in acceptable_inputs:
            player2_guess_y = input(f"{player2_name}, enter a y coordinate for where you think {player1_name}'s ship is: ")
            if player2_guess_y not in acceptable_inputs:        
                print('Please enter a digit between 1 and 10!')

        os.system("clear")

        player2_guess_x = int(player2_guess_x)
        player2_guess_y = int(player2_guess_y)
        g.input_by_player2(player2_guess_x, player2_guess_y, player1_set_x, player1_set_y)

        if player2_guess_x == player1_set_x and player2_guess_y == player1_set_y:
            print("{player2_name}, you are the winner!")
            break
        
    print(f"\nThanks {player1_name} and {player2_name} for playing the battleship!\n")


if __name__== '__main__':
    user_gameplay()
