
from tkinter import *
import time

cash = 0
clickersBought = 0
clickerWorkTime = 15
clickerCost = 10
clickerCostMultiplier = 1


def hideMe(sth):
    sth.pack_forget()


def click():
    global cash
    cash += 1
    cashDisplayV.set("Cash: $" + str(cash))
    print(cash)

def shopUI():
    hideMe(shop)
    hideMe(click)
    back.pack()
    buy.pack()
    clickerNum.pack()


def clicker():
    cash += clickersBought
    time.sleep(clickerWorkTime)


def normalUI():
    hideMe(back)
    hideMe(buy)
    hideMe(clickerNum)
    click.pack(anchor=CENTER)
    cashDisplay.pack(anchor=NE)
    shop.pack()

def buyClicker():
    global cash
    global clickersBought
    global clickerWorkTime
    global clickerCost
    global clickerCostMultiplier
    clickerWorkTime -= 0.1
    costDisplayV.set("Next Clicker: $" + str(clickerCost))
    clickersBoughtV.set("Clickers Bought: " + str(clickersBought))
    if clickerCost > cash:
        pass
    else:
        cash -= clickerCost
        clickersBought += 1
        clickerCost += clickerCostMultiplier
        clickerCostMultiplier += 1
        cashDisplayV.set("Cash: $" + str(cash))
        cashDisplay.pack()

print("Please wait 15 seconds.")
Game = Tk()

Game.title("Garry's Clicker")
global costDisplayV
screenHeight = Game.winfo_screenheight()
screenWidth = Game.winfo_screenwidth()
geometry = "%dx%d" % (screenWidth, screenHeight)

Game.geometry(geometry)


buy = Button(Game, text="Buy Clicker", command=buyClicker)
back = Button(Game, text="Back", command=normalUI)
click = Button(Game, text="Click", command=click, padx=10, pady=10)
cashDisplayV = StringVar()
clickersBoughtV = StringVar()
costDisplayV = StringVar()
shop = Button(Game, text="Shop", command=shopUI)
cashDisplay = Label(Game, textvariable=cashDisplayV, font=("Helvetica", 24))
clickerNum = Label(Game, textvariable=clickersBoughtV, font=("Helvetica", 24))
clickerCostDisplay = Label(Game, textvariable=costDisplayV, font=("Helvetica", 24))
cashDisplay.pack(anchor=NE)
click.pack(anchor=CENTER)
shop.pack()

clicker()

Game.mainloop()
