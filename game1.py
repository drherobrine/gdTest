<<<<<<< HEAD
from tkinter import *
=======
from Tkinter import *
>>>>>>> b4d32e4ccb74fcf283d7ad69738d05a18670e901
import time

cash = 0
clickersBought = 0
<<<<<<< HEAD
clickerWorkTime = 15


def hideMe(sth):
    sth.pack_forget()
=======
>>>>>>> b4d32e4ccb74fcf283d7ad69738d05a18670e901


def click():
    global cash
    cash += 1
<<<<<<< HEAD
    cashDisplayV.set("Cash: " +str(cash))
    print(cash)


def shopUI():
    hideMe(shop)
    hideMe(click)

Game = Tk()

screenHeight = Game.winfo_screenheight()
screenWidth = Game.winfo_screenwidth()
geometry = "%dx%d" % (screenWidth, screenHeight)

Game.geometry(geometry)

click = Button(Game, text="Click", command=click, padx=10, pady=10)
cashDisplayV = StringVar()
shop = Button(Game, text="Shop")
shop.bind('<Button-1>', shopUI)
cashDisplay = Label(Game, textvariable=cashDisplayV, font=("Helvetica", 24))
cashDisplay.pack(anchor=NE)
click.pack(anchor=CENTER)
shop.pack()


Game.mainloop()







=======
    print cash


Game = Tk()

click = Button(Game, text="Click", command=click)

cashDisplay = Label(Game, textvariable=cash)
cashDisplay.pack(anchor=NW)
click.pack(anchor=CENTER)
Game.mainloop()
>>>>>>> b4d32e4ccb74fcf283d7ad69738d05a18670e901
