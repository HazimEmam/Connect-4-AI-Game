import random

EMPTY = 0
RED = 1
BLUE = 2

class AlphaBeta:

    def getUtility(self ,board):
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
                        if board[i][k] == RED:
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

        return maxRed - maxBlue
    
    def insertPiece(self ,board, column, piece):
        newBoard = [row.copy() for row in board]
        for i in reversed(range(0, 6)):
            if newBoard[i][column] == EMPTY:
                newBoard[i][column] = piece
                break
        return newBoard


    def alphaBetaPruning(self ,board, minOrMax, maxDepth, alpha , beta, currentDepth=1):
        if minOrMax == "min" and self.gameOver(board):
            return 5
        elif minOrMax == "max" and self.gameOver(board):
            return -5
        if currentDepth == maxDepth:
            return self.getUtility(board)
        if minOrMax == "max":
            currentUtility = -999999
            for i in range(0, 7):
                if (board[0][i] == EMPTY):
                    newBoard = self.insertPiece(board, i, RED)
                    if self.gameOver(newBoard):
                        currentUtility =4
                    else:
                        currentUtility = max(currentUtility,self.alphaBetaPruning(newBoard,"min", maxDepth, alpha , beta, currentDepth + 1))
                    if(currentUtility > beta):
                        break
                    alpha = max(alpha,currentUtility)

            if( currentUtility == -999999):
                return self.getUtility(board)
            else :
                return currentUtility
        else:
            currentUtility = 999999
            for i in range(0, 7):
                newBoard = self.insertPiece(board, i, BLUE)
                if self.gameOver(newBoard):
                    currentUtility = -4
                else:
                    currentUtility = min(currentUtility,self.alphaBetaPruning(newBoard,"max", maxDepth, alpha , beta, currentDepth + 1))
                if(currentUtility < alpha):
                    break
                beta = min(beta,currentUtility)
            if( currentUtility == 999999):
                return self.getUtility(board)
            else :
                return currentUtility
            
            
    
    def chooseColumn(self , board, maxDepth):
        arr = []
        for i in range(0, 7):
            if board[0][i] == EMPTY:
                newBoard = self.insertPiece(board, i, RED)
                currentUtility = self.alphaBetaPruning(newBoard, "min", maxDepth, -999999 , 999999)
                pair = (currentUtility, i)
                arr.append(pair)
        print(arr)
        newArr = self.getMaxElements(arr)
        print(newArr)
        return newArr[int((len(newArr)-1)/2)][1]
    
    def printBoard(self,board):
        print(" ", end="")
        for i in range(0, 7):
            print(" ", i, end="")
        print()
        for i in range(0, len(board)):
            print(i, " ", end="")
            for j in range(0, len(board[i])):
                print(board[i][j], end="  ")
            print()

    def getMaxElements(self,arr):
        maxElement = -5
        newArr = []
        for i in range(0, len(arr)):
            if arr[i][0] > maxElement:
                maxElement = arr[i][0]
        for i in range(0, len(arr)):
            if arr[i][0] == maxElement:
                newArr.append(arr[i])
        return newArr

    def gameOver(self , board):
        for i in range(0, 6):
            for j in range(0, 7):
                if j < 4 and board[i][j] == RED and board[i][j+1] == RED and board[i][j+2] == RED and board[i][j+3] == RED:
                    return True
                elif j < 4 and board[i][j] == BLUE and board[i][j+1] == BLUE and board[i][j+2] == BLUE and board[i][j+3] == BLUE:
                    return True
                if i < 3 and board[i][j] == RED and board[i+1][j] == RED and board[i+2][j] == RED and board[i+3][j] == RED:
                    return True
                elif i < 3 and board[i][j] == BLUE and board[i+1][j] == BLUE and board[i+2][j] == BLUE and board[i+3][j] == BLUE:
                    return True
                if j < 4 and i < 3 and board[i][j] == RED and board[i+1][j+1] == RED and board[i+2][j+2] == RED and board[i+3][j+3] == RED:
                    return True
                elif j < 4 and i < 3 and board[i][j] == BLUE and board[i+1][j+1] == BLUE and board[i+2][j+2] == BLUE and board[i+3][j+3] == BLUE:
                    return True
                if j > 2 and i < 3 and board[i][j] == RED and board[i+1][j-1] == RED and board[i+2][j-2] == RED and board[i+3][j-3] == RED:
                    return True
                elif j > 2 and i < 3 and board[i][j] ==BLUE and board[i+1][j-1] == BLUE and board[i+2][j-2] == BLUE and board[i+3][j-3] == BLUE:
                    return True
        return False

