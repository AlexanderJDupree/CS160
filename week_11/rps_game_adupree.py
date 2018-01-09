# file: rps_game_adupree.py
# description: Rock, Paper, Scissors game in tkinter GUI
# authors: Alex DuPree
# date: 12/04/2017
# compiler: Python 3.6

from tkinter import *
from random import randint


def computer_choice():
    options = {1: "rock", 2: "paper", 3: "scissors"}
    return options[randint(1, 3)]


def game_eval(computer, player):
    choices = {
        ("rock", "paper"): True, ("rock", "scissors"): False,
        ("paper", "rock"): False, ("paper", "scissors"): True,
        ("scissors", "rock"): True, ("scissors", "paper"): False
    }
    try:
        return choices[(computer, player)]
    except KeyError:
        return None


def show_winner(computer, win=None):
    if win == False:
        return "You Lost, Computer chose {}.".format(computer)
    elif win == True:
        return "You Won! Computer chose {}.".format(computer)
    else:
        return "It's a tie! Computer chose {}.".format(computer)


def rockButton():
    playerChoice = 'rock'
    play_game(playerChoice)


def paperButton():
    playerChoice = 'paper'
    play_game(playerChoice)


def scissorButton():
    playerChoice = 'scissors'
    play_game(playerChoice)


def play_game(playerChoice):
    computer = computer_choice()
    game_outcome = game_eval(computer, playerChoice)
    winner = show_winner(computer, game_outcome)
    strVar.set(winner)


root = Tk()
root.title("MY FIRST GAME")
root.geometry("300x150")

topFrame = Frame(root).pack(side=TOP)
bottomFrame = Frame(root).pack(side=BOTTOM)

label = Label(topFrame, text="ROCK PAPER SCISSORS",
              fg='white', bg='blue').pack()

playerChoice = ""
strVar = StringVar()

rock = Button(bottomFrame, text="Rock",
              command=rockButton).place(x=30, y=50)

paper = Button(bottomFrame, text="Paper",
               command=paperButton).place(x=130, y=50)

scissors = Button(bottomFrame, text="Scissors",
                  command=scissorButton).place(x=230, y=50)

endLabel = Label(bottomFrame, textvariable=strVar).pack(side=BOTTOM)

root.mainloop()
