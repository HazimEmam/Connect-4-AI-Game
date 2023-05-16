from PIL import ImageGrab
import pyautogui

# YOU MAY NEED TO CHANGE THESE VALUES BASED ON YOUR SCREEN SIZE
LEFT = 415
TOP = 170
RIGHT = 950
BOTTOM = 635

EMPTY = 0
RED = 1
BLUE = 2


class Board:
    def __init__(self) -> None:
        self.board = [[EMPTY for i in range(7)] for j in range(6)]
        # code to initialize empty board:-
        for i in range(0, 6):
            for j in range(0, 7):
                self.board[i][j] = '*'

    def print_grid(self):
        print(" ", end="")
        for i in range(0, 7):
            print(" ", i, end="")
        print()
        for i in range(0, len(self.board)):
            print(i, " ", end="")
            for j in range(0, len(self.board[i])):
                print(self.board[i][j], end="  ")
            print()

    def _convert_grid_to_color(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == (255, 255, 255):
                    grid[i][j] = EMPTY
                elif grid[i][j][0] > 200:
                    grid[i][j] = RED
                elif grid[i][j][0] > 50:
                    grid[i][j] = BLUE
        return grid

    def _get_grid_cordinates(self):
        startCord = (50, 55)
        cordArr = []
        for i in range(0, 7):
            for j in range(0, 6):
                x = startCord[0] + i * 76
                y = startCord[1] + j * 72
                cordArr.append((x, y))
        return cordArr

    def _transpose_grid(self, grid):
        return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]

    def _capture_image(self):
        image = ImageGrab.grab()
        cropedImage = image.crop((LEFT, TOP, RIGHT, BOTTOM))
        return cropedImage

    def _convert_image_to_grid(self, image):
        pixels = [[] for i in range(7)]
        i = 0
        for index, cord in enumerate(self._get_grid_cordinates()):
            pixel = image.getpixel(cord)
            if index % 6 == 0 and index != 0:
                i += 1
            pixels[i].append(pixel)
        return pixels

    def _get_grid(self):
        cropedImage = self._capture_image()
        pixels = self._convert_image_to_grid(cropedImage)
        # cropedImage.show()
        grid = self._transpose_grid(pixels)
        return grid

    def _check_if_game_end(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == EMPTY and self.board[i][j] != EMPTY:
                    return True
        return False

    def get_game_grid(self):
        game_grid = self._get_grid()
        new_grid = self._convert_grid_to_color(game_grid)
        is_game_end = self._check_if_game_end(new_grid)
        self.board = new_grid
        return (self.board, is_game_end)

    def select_column(self, column):
        pyautogui.click(
            self._get_grid_cordinates()[column][1] + LEFT,
            self._get_grid_cordinates()[column][0] + TOP,
        )

    def utilityFunction(self):
        Utility = 0
        # Calculate max Red in 4 consecutive cells
        maxRed = 0
        for i in range(0, 6):
            for j in range(0, 7):
                if j < 4:
                    currentStreak = 0
                    for k in range(j, j+4):
                        if self.board[i][k] == 'B':
                            currentStreak = 0
                            break
                        if self.board[i][k] == 'R':
                            currentStreak += 1
                    maxRed = max(maxRed, currentStreak)
                if i < 3:
                    currentStreak = 0
                    for k in range(i, i+4):
                        if self.board[k][j] == 'B':
                            currentStreak = 0
                            break
                        if self.board[k][j] == 'R':
                            currentStreak += 1
                    maxRed = max(maxRed, currentStreak)
                if j < 4 and i < 3:
                    currentStreak = 0
                    for k, l in zip(range(i, i+4), range(j, j+4)):
                        if self.board[k][l] == 'B':
                            currentStreak = 0
                            break
                        if self.board[k][l] == 'R':
                            currentStreak += 1
                    maxRed = max(maxRed, currentStreak)
                if j > 2 and i < 3:
                    currentStreak = 0
                    for k, l in zip(range(i, i+4), reversed(range(j-3, j+1))):
                        if self.board[k][l] == 'B':
                            currentStreak = 0
                            break
                        if self.board[k][l] == 'R':
                            currentStreak += 1
                    maxRed = max(maxRed, currentStreak)
        maxBlue = 0
        for i in range(0, 6):
            for j in range(0, 7):
                if j < 4:
                    currentStreak = 0
                    for k in range(j, j + 4):
                        if self.board[i][k] == 'R':
                            currentStreak = 0
                            break
                        if self.board[i][k] == 'B':
                            currentStreak += 1
                    maxBlue = max(maxBlue, currentStreak)
                if i < 3:
                    currentStreak = 0
                    for k in range(i, i + 4):
                        if self.board[k][j] == 'R':
                            currentStreak = 0
                            break
                        if self.board[k][j] == 'B':
                            currentStreak += 1
                    maxBlue = max(maxBlue, currentStreak)
                if j < 4 and i < 3:
                    currentStreak = 0
                    for k, l in zip(range(i, i + 4), range(j, j + 4)):
                        if self.board[k][l] == 'R':
                            currentStreak = 0
                            break
                        if self.board[k][l] == 'B':
                            currentStreak += 1
                    maxBlue = max(maxBlue, currentStreak)
                if j > 2 and i < 3:
                    currentStreak = 0
                    for k, l in zip(range(i, i + 4), reversed(range(j - 3, j + 1))):
                        if self.board[k][l] == 'R':
                            currentStreak = 0
                            break
                        if self.board[k][l] == 'B':
                            currentStreak += 1
                    maxBlue = max(maxBlue, currentStreak)

        return maxRed - maxBlue
