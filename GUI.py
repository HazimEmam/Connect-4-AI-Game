# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import tkinter as tk

root = tk.Tk()
root.title("Difficulty Selection")

# Set the window size and position
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_pos = int((screen_width/2) - (WINDOW_WIDTH/2))
y_pos = int((screen_height/2) - (WINDOW_HEIGHT/2))
root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x_pos}+{y_pos}')

# Define the callback functions for each button
def select_easy():
    print("Easy mode selected")


def select_medium():
    print("Medium mode selected")


def select_hard():
    print("Hard mode selected")

# Create the buttons and add them to the window
button_easy = tk.Button(root, text="Easy", command=select_easy, width=20, height=3)
button_medium = tk.Button(root, text="Medium", command=select_medium, width=20, height=3)
button_hard = tk.Button(root, text="Hard", command=select_hard, width=20, height=3)

# Center the buttons horizontally and vertically
button_width = 120
button_height = 80
x_pos = (WINDOW_WIDTH - button_width) / 2
y_pos = (WINDOW_HEIGHT - button_height * 3 - 20) / 2

button_easy.place(x=x_pos, y=y_pos, width=button_width, height=button_height)
button_medium.place(x=x_pos, y=y_pos + button_height + 10, width=button_width, height=button_height)
button_hard.place(x=x_pos, y=y_pos + button_height * 2 + 20, width=button_width, height=button_height)

# Start the main loop
root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
