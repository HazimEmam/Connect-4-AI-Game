from tkinter import *
import tkinter as tk
from board import Board
import time
import random
from alphaBeta import AlphaBeta
from MinMax import MinMax

class GUIGame:
    def __init__(self):
        self.selectedAlgorithm = "MiniMax"
        self.diff = "easy"
        self.root = root
        self.root.geometry('400x500+800+200')
        self.root.title('Difficulty Selection')
        self.root.configure(background="#4C4C6D")
        self.root.resizable(False,False)
        algTitle=Label(self.root, text='Choose Algorithm' , bg='#1B9C85',font=('monospace',14),fg='#FFE194')
        algTitle.pack(fill=X)
        #------optionBox-------
        algoFrame = Frame(self.root,background='#E8F6EF')
        algoFrame.place(x=125 , y=30 , width=150 , height= 30)

        options = ["MiniMax", "AlphaBeta pruning"]
        algorithm = tk.StringVar(algoFrame)
        algorithm.set(options[0])
        algoChoose = tk.OptionMenu(algoFrame, algorithm, *options, command=self.on_select)
        algoChoose.pack()

        #------DifficultyFrame---
        diffFrame = Frame(self.root,background='#E8F6EF')
        diffFrame.place(x=50 , y=100 , width=300 , height=350)
        diffTitle=Label(diffFrame, text='Choose Difficulty' , bg='#1B9C85',font=('monospace',10),fg='#FFE194')
        diffTitle.pack(fill=X)

        easyButton=Button(diffFrame,text='Easy',command=lambda: self.select_easy())
        easyButton.place(x=75 , y = 60 , width=150 , height=50)
        mediamButton=Button(diffFrame,text='Medium',command=self.select_medium)
        mediamButton.place(x=75 , y = 120 , width=150 , height=50)
        HardButton=Button(diffFrame,text='Hard',command=self.select_hard)
        HardButton.place(x=75 , y = 180 , width=150 , height=50)
        playButton=Button(diffFrame,text='Play',command=self.play)
        playButton.place(x=100 , y = 240 , width=100 , height=50)

    def on_select(self,value):
        #print(value, "Algorithm was Selected")
        self.selectedAlgorithm = value

    def select_easy(self):
        #print("Easy mode selected")
        self.diff="easy"


    def select_medium(self):
        #print("Medium mode selected")
        self.diff="medium"

    def select_hard(self):
        #print("Hard mode selected")
        self.diff="hard"


    def play(self):
        board = Board()
        if self.selectedAlgorithm == "AlphaBeta pruning":
            algo = AlphaBeta()
            maxDepth=0
            if self.diff == "easy":
                maxDepth = 2
            elif self.diff == "medium":
                maxDepth = 4
            elif self.diff == "hard":
                maxDepth = 6
            time.sleep(2)
            game_end = False
            while not game_end:
                (game_board, game_end) = board.get_game_grid()
                board.print_grid(game_board)
                time.sleep(2)
                selected_column = algo.chooseColumn(game_board,maxDepth)
                board.select_column(selected_column)
                time.sleep(2)
        else:
            algo=MinMax()
            maxDepth=0
            if self.diff == "easy":
                maxDepth = 2
            elif self.diff == "medium":
                maxDepth = 4
            elif self.diff == "hard":
                maxDepth = 5
            time.sleep(2)
            game_end = False
            while not game_end:
                (game_board, game_end) = board.get_game_grid()
                board.print_grid(game_board)
                time.sleep(2)
                selected_column = algo.chooseColumn(game_board,maxDepth)
                board.select_column(selected_column)
                time.sleep(2)


root=Tk()
obj=GUIGame()
root.mainloop()