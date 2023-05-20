from board import Board
import time
import random
from alphaBeta import AlphaBeta
from MinMax import MinMax
#from MinMax import MinMax

# GAME LINK
# http://kevinshannon.com/connect4/


def main():
    board = Board()
    #(game_board, game_end) = board.get_game_grid()
    #board.print_grid(game_board)
    alpha = AlphaBeta()
    min = MinMax()
    #check =alpha.alphaBetaPruning(game_board,"max",1)
    #board.print_grid(game_board)
    #print(check)
    #col = alpha.chooseColumn(game_board,3)
    #print(col)
    
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
        selected_column = alpha.chooseColumn(game_board,6)
        print("selected column = ",selected_column)
        board.select_column(selected_column)

        time.sleep(2)
    

if __name__ == "__main__":
    main()
