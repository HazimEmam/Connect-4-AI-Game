import random
import boardWithUtilityFunction

EMPTY = 0
RED = 1
BLUE = 2

class MinMax:

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


    def minMax(self ,board, minOrMax, maxDepth, currentDepth=1):
        if minOrMax == "min" and self.gameOver(board):
            return 5
        elif minOrMax == "max" and self.gameOver(board):
            return -5
        if currentDepth == maxDepth:
            return self.getUtility(board)
        arr = []
        for i in range(0, 7):
            if minOrMax == "max" and board[0][i] == EMPTY:
                newBoard = self.insertPiece(board, i, RED)
                if self.gameOver(newBoard):
                    arr.append(4)
                else:
                    currentUtility = self.minMax(newBoard, "min", maxDepth, currentDepth + 1)
                    arr.append(currentUtility)
            elif board[0][i] == EMPTY:
                newBoard = self.insertPiece(board, i, BLUE)
                if self.gameOver(newBoard):
                    arr.append(-4)
                else:
                    currentUtility = self.minMax(newBoard, "max", maxDepth, currentDepth + 1)
                    arr.append(currentUtility)
        arr = sorted(arr)
        #print ("array = " ,arr)
        if len(arr) == 0 :
            return self.getUtility(board)
        if minOrMax == "max":
            return arr[-1]
        else:
            return arr[0]



    def chooseColumn(self , board, maxDepth):
        arr = []
        for i in range(0, 7):
            if board[0][i] == EMPTY:
                newBoard = self.insertPiece(board, i, RED)
                currentUtility = self.minMax(newBoard, "min", maxDepth)
                pair = (currentUtility, i)
                arr.append(pair)
        print(arr)
        newArr = self.getMaxElements(arr)
        print(newArr)
        return newArr[int((len(newArr)-1)/2)][1]
        
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


