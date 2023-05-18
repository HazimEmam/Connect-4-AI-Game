from board import Board
import time
import random


# GAME LINK
# http://kevinshannon.com/connect4/

def getUtility(board):
    Utility = 0
    # Calculate max Red in 4 consecutive cells
    maxRed = 0
    for i in range(0, 6):
        for j in range(0, 7):
            if j < 4:
                currentStreak = 0
                for k in range(j, j + 4):
                    if board[i][k] == 'B':
                        currentStreak = 0
                        break
                    if board[i][k] == 'R':
                        currentStreak += 1
                maxRed = max(maxRed, currentStreak)
            if i < 3:
                currentStreak = 0
                for k in range(i, i + 4):
                    if board[k][j] == 'B':
                        currentStreak = 0
                        break
                    if board[k][j] == 'R':
                        currentStreak += 1
                maxRed = max(maxRed, currentStreak)
            if j < 4 and i < 3:
                currentStreak = 0
                for k, l in zip(range(i, i + 4), range(j, j + 4)):
                    if board[k][l] == 'B':
                        currentStreak = 0
                        break
                    if board[k][l] == 'R':
                        currentStreak += 1
                maxRed = max(maxRed, currentStreak)
            if j > 2 and i < 3:
                currentStreak = 0
                for k, l in zip(range(i, i + 4), reversed(range(j - 3, j + 1))):
                    if board[k][l] == 'B':
                        currentStreak = 0
                        break
                    if board[k][l] == 'R':
                        currentStreak += 1
                maxRed = max(maxRed, currentStreak)
    maxBlue = 0
    for i in range(0, 6):
        for j in range(0, 7):
            if j < 4:
                currentStreak = 0
                for k in range(j, j + 4):
                    if board[i][k] == 'R':
                        currentStreak = 0
                        break
                    if board[i][k] == 'B':
                        currentStreak += 1
                maxBlue = max(maxBlue, currentStreak)
            if i < 3:
                currentStreak = 0
                for k in range(i, i + 4):
                    if board[k][j] == 'R':
                        currentStreak = 0
                        break
                    if board[k][j] == 'B':
                        currentStreak += 1
                maxBlue = max(maxBlue, currentStreak)
            if j < 4 and i < 3:
                currentStreak = 0
                for k, l in zip(range(i, i + 4), range(j, j + 4)):
                    if board[k][l] == 'R':
                        currentStreak = 0
                        break
                    if board[k][l] == 'B':
                        currentStreak += 1
                maxBlue = max(maxBlue, currentStreak)
            if j > 2 and i < 3:
                currentStreak = 0
                for k, l in zip(range(i, i + 4), reversed(range(j - 3, j + 1))):
                    if board[k][l] == 'R':
                        currentStreak = 0
                        break
                    if board[k][l] == 'B':
                        currentStreak += 1
                maxBlue = max(maxBlue, currentStreak)

    return maxRed - maxBlue


def insertPiece(board, column, piece):
    newBoard = [row.copy() for row in board]
    for i in reversed(range(0, 6)):
        if newBoard[i][column] == '*':
            newBoard[i][column] = piece
            break
    return newBoard


def minMax(board, minOrMax, maxDepth, currentDepth=1):
    if currentDepth == maxDepth:
        return getUtility(board)
    arr = []
    for i in range(0, 7):
        if minOrMax == "max":
            newBoard = insertPiece(board, i, 'R')
            currentUtility = minMax(newBoard, "min", maxDepth, currentDepth + 1)
            arr.append(currentUtility)
        else:
            newBoard = insertPiece(board, i, 'B')
            currentUtility = minMax(newBoard, "max", maxDepth, currentDepth + 1)
            arr.append(currentUtility)
    arr = sorted(arr)
    #print(arr)
    if minOrMax == "max":
        return arr[-1]
    else:
        return arr[0]


def chooseColumn(board, maxDepth):
    arr = []
    for i in range(0, 7):
        #printBoard(board)
        newBoard = insertPiece(board, i, 'R')
        currentUtility = minMax(newBoard, "min", maxDepth)
        pair = (currentUtility, i)
        arr.append(pair)
    arr = sorted(arr)
    print(arr)
    return arr[-1][1]


def test():
    pair = (4, -1)
    pair2 = (6, -2)
    pair3 = (4, -2)
    arr = [pair, pair2, pair3]
    arr = sorted(arr)
    print(arr[-1][0])


def printBoard(board):
    print(" ", end="")
    for i in range(0, 7):
        print(" ", i, end="")
    print()
    for i in range(0, len(board)):
        print(i, " ", end="")
        for j in range(0, len(board[i])):
            print(board[i][j], end="  ")
        print()

def main():
    # board = Board()
    b = Board()
    # i=0
    # j=3
    # for k, l in zip(range(i, i+4), reversed(range(j-3, j+1))):
    # print(k, l)

    # b.board=insertPiece(b.board, 5, 'B')
    # b.print_grid()
    #test()
    while True:
        x = 0
        y = 0
        z = '*'
        x = int(input())
        y = int(input())
        z = input()
        b.board[x][y] = z
        # b.board = insertPiece(b.board, 5, 'B')
        b.print_grid()
        print(getUtility(b.board))
        #minMax(b.board, "max", 1)
        #print(chooseColumn(b.board, 1))

    # time.sleep(2)
    # game_end = False
    # while not game_end:
    # (game_board, game_end) = board.get_game_grid()

    # FOR DEBUG PURPOSES
    # board.print_grid(game_board)
    # print("\n", "\n")

    # time.sleep(5)

    # YOUR CODE GOES HERE

    # Insert here the action you want to perform based on the output of the algorithm
    # You can use the following function to select a column
    # random_column = random.randint(0, 6)
    # board.select_column(random_column)

    # time.sleep(2)


if __name__ == "__main__":
    main()
