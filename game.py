from Tkinter import *
import time

cash = 0
clickersBought = 0


def click():
    global cash
    cash += 1
    print cash


Game = Tk()

click = Button(Game, text="Click", command=click)

cashDisplay = Label(Game, textvariable=cash)
cashDisplay.pack(anchor=NW)
click.pack(anchor=CENTER)
Game.mainloop()
