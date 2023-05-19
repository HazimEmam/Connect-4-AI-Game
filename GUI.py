# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import tkinter as tk

root = tk.Tk()
root.title("Difficulty Selection")


# Create a variable to store the selected option
option = tk.StringVar(value="Option 1")
option = tk.StringVar(value="Option 2")


# Set the window size and position
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_pos = int((screen_width/2) - (WINDOW_WIDTH/2))
y_pos = int((screen_height/2) - (WINDOW_HEIGHT/2))
root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x_pos}+{y_pos}')

# Define the callback functions for each button
def select_MinMax():
    print("MinMax Algorithm")

def select_AlphaBeta():
    print("AlphaBeta Algorthim")

def select_easy():
    print("Easy mode selected")


def select_medium():
    print("Medium mode selected")


def select_hard():
    print("Hard mode selected")


# Create the radio buttons
rb1 = tk.Radiobutton(root, text="MinMax Algorithm",command = select_MinMax ,variable=option, value="MinMax Algorithm")
rb2 = tk.Radiobutton (root, text="AlphaBeta Algorithm",command = select_AlphaBeta ,variable=option, value="AlphaBeta Algorithm")

# Create the buttons and add them to the window
button_easy = tk.Button(root, text="Easy", command=select_easy, width=20, height=3)
button_medium = tk.Button(root, text="Medium", command=select_medium, width=20, height=3)
button_hard = tk.Button(root, text="Hard", command=select_hard, width=20, height=3)

rb1.pack(side="top")
rb2.pack(side="top", padx=50, pady=0)
button_easy.pack(side="top",pady=10)
button_medium.pack(side= "top",pady=10)
button_hard.pack(side= "top",pady=10)


# Start the main loop
root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
