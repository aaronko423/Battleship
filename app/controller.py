#! usr/bin/env python3

from gameboard import GameBoard
g = GameBoard()

def user():

    guess = 0
    x_input = None
    y_input = None
    acceptable_x = ["0", "1", "2", "3", "4"]
    acceptable_y = ["0", "1", "2", "3", "4"]    

    while x_input != g.x_ran or y_input != g.y_ran:
        
        print("\nMake your battleship attack!\n")

        while x_input not in acceptable_x:
            x_input = input('Enter an x coordinate for where you think the ship is: ')
            if x_input not in acceptable_x:
                print('Please enter a digit between 0 and 4!')    
        
        while y_input not in acceptable_y:
            y_input = input('Enter an y coordinate for where you think the ship is: ')
            if y_input not in acceptable_y:        
                print('Please enter a digit between 0 and 4!')

        x_input = int(x_input)
        y_input = int(y_input)
        g.input(x_input, y_input)
        
        guess +=1
    
    if guess == 1:
        print (f"Game Over. You won on the first try!!!\n")
    else:
        print (f"Game Over. You won!!! \nIt took you {guess} guesses\n")


if __name__== '__main__':
    user()
