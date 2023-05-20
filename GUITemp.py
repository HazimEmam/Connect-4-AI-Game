from tkinter import *
import tkinter as tk

class GUIGame:
    def __init__(self):
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


        def on_select(value):
            print(value, "Algorithm was Selected")
        

        options = ["MiniMax", "AlphaBeta pruning"]
        algorithm = tk.StringVar(algoFrame)
        algorithm.set(options[0])
        algoChoose = tk.OptionMenu(algoFrame, algorithm, *options, command=on_select)
        algoChoose.pack()

        #------DifficultyFrame--------
        diffFrame = Frame(self.root,background='#E8F6EF')
        diffFrame.place(x=50 , y=100 , width=300 , height=350)
        diffTitle=Label(diffFrame, text='Choose Difficulty' , bg='#1B9C85',font=('monospace',10),fg='#FFE194')
        diffTitle.pack(fill=X)
        def select_easy():
            print("Easy mode selected")


        def select_medium():
            print("Medium mode selected")


        def select_hard():
            print("Hard mode selected")

        easyButton=Button(diffFrame,text='Easy',command=select_easy)
        easyButton.place(x=75 , y = 80 , width=150 , height=50)
        mediamButton=Button(diffFrame,text='Mediam',command=select_medium)
        mediamButton.place(x=75 , y = 160 , width=150 , height=50)
        HardButton=Button(diffFrame,text='Hard',command=select_hard)
        HardButton.place(x=75 , y = 240 , width=150 , height=50)


root=Tk()
obj=GUIGame()
root.mainloop()