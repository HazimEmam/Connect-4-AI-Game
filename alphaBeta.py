import random

EMPTY = 0
RED = 1
BLUE = 2

class AlphaBeta:

    def getUtility(self ,board):
        #b = Board()
        #b.print_grid(board)
        Utility = 0
        # Calculate max Red in 4 consecutive cells
        maxRed = 0
        for i in range(0, 6):
            for j in range(0, 7):
                if j < 4:
                    currentStreak = 0
                    for k in range(j, j + 4):
                        if board[i][k] == BLUE:
                            currentStreak = 0
                            break
                        if board[i][k] == RED :
                            currentStreak += 1
                    maxRed = max(maxRed, currentStreak)
                if i < 3:
                    currentStreak = 0
                    for k in range(i, i + 4):
                        if board[k][j] == BLUE:
                            currentStreak = 0
                            break
                        if board[k][j] == RED:
                            currentStreak += 1
                    maxRed = max(maxRed, currentStreak)
                if j < 4 and i < 3:
                    currentStreak = 0
                    for k, l in zip(range(i, i + 4), range(j, j + 4)):
                        if board[k][l] == BLUE:
                            currentStreak = 0
                            break
                        if board[k][l] == RED:
                            currentStreak += 1
                    maxRed = max(maxRed, currentStreak)
                if j > 2 and i < 3:
                    currentStreak = 0
                    for k, l in zip(range(i, i + 4), reversed(range(j - 3, j + 1))):
                        if board[k][l] == BLUE:
                            currentStreak = 0
                            break
                        if board[k][l] == RED:
                            currentStreak += 1
                    maxRed = max(maxRed, currentStreak)
        maxBlue = 0
        for i in range(0, 6):
            for j in range(0, 7):
                if j < 4:
                    currentStreak = 0
                    for k in range(j, j + 4):
                        if board[i][k] == RED:
                            currentStreak = 0
                            break
                        if board[i][k] == BLUE:
                            currentStreak += 1
                    maxBlue = max(maxBlue, currentStreak)
                if i < 3:
                    currentStreak = 0
                    for k in range(i, i + 4):
                        if board[k][j] == RED:
                            currentStreak = 0
                            break
                        if board[k][j] == BLUE:
                            currentStreak += 1
                    maxBlue = max(maxBlue, currentStreak)
                if j < 4 and i < 3:
                    currentStreak = 0
                    for k, l in zip(range(i, i + 4), range(j, j + 4)):
                        if board[k][l] == RED:
                            currentStreak = 0
                            break
                        if board[k][l] == BLUE:
                            currentStreak += 1
                    maxBlue = max(maxBlue, currentStreak)
                if j > 2 and i < 3:
                    currentStreak = 0
                    for k, l in zip(range(i, i + 4), reversed(range(j - 3, j + 1))):
                        if board[k][l] == RED:
                            currentStreak = 0
                            break
                        if board[k][l] == BLUE:
                            currentStreak += 1
                    maxBlue = max(maxBlue, currentStreak)

        if(maxBlue == 3):
            return -3
        return maxRed - maxBlue
    
    def insertPiece(self ,board, column, piece):
        newBoard = [row.copy() for row in board]
        for i in reversed(range(0, 6)):
            if newBoard[i][column] == 0:
                newBoard[i][column] = piece
                break
        return newBoard


    def alphaBetaPruning(self ,board, minOrMax, maxDepth, alpha , beta, currentDepth=1):
        if currentDepth == maxDepth:
            return self.getUtility(board)
        
        for i in range(0, 7):
            if minOrMax == "max":
                alpha = -999999
                newBoard = self.insertPiece(board, i, RED)
                #print("new board " ,i+1 ,newBoard)
                #print(newBoard)
                currentUtility = self.alphaBetaPruning(newBoard, "min", maxDepth, alpha , beta ,currentDepth + 1)
                alpha = max(alpha,currentUtility)
                if(beta <= alpha):
                    break
            else:
                beta = 999999
                newBoard = self.insertPiece(board, i, BLUE)
                currentUtility = self.alphaBetaPruning(newBoard, "max", maxDepth,alpha , beta,currentDepth + 1)
                beta = min(beta ,currentUtility)
                
                if(beta <= alpha):
                    break

        #print("alpha : ",alpha ,", beta : ", beta)
        if minOrMax == "max":
            return alpha
        else:
            return beta


    def chooseColumn(self , board, maxDepth):
        arr = []
        for i in range(0, 7):
            #printBoard(board)
            newBoard = self.insertPiece(board, i, RED)
            currentUtility = self.alphaBetaPruning(newBoard, "min", maxDepth , -999999 , 999999)
            pair = (currentUtility, i)
            arr.append(pair)
        arr = sorted(arr)
        print(arr)
        newArr = self.getMaxArray(arr)
        return random.choice(newArr)
    
    def getMaxArray(self ,arr):
        newArr =[]
        max = arr[-1][0]
        for i in range (0,7):
            if arr[i][0] == max:
                newArr.append(arr[i][1])

        print(newArr)
        return newArr

