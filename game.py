from board import Board
import time
import random
from GUITemp import GUIGame
from alphaBeta import AlphaBeta
from MinMax import MinMax

# GAME LINK
# http://kevinshannon.com/connect4/

def main():
    
    board = Board()
    alpha = AlphaBeta()
    min = MinMax()
    
    Gui = GUIGame()
    time.sleep(2)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()

        # FOR DEBUG PURPOSES
        board.print_grid(game_board)
        time.sleep(2)

        # YOUR CODE GOES HERE

        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the following function to select a column
        selected_column = alpha.chooseColumn(game_board,4)
        print("selected :" , selected_column)
        board.select_column(selected_column)

        time.sleep(2)
    

if __name__ == "__main__":
    main()
