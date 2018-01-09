# file: rock_paper_scissors.py
# description: play a game of rock paper scissors
# author: Alexander DuPree
# date: 11 / 15 / 2017
# compiler: Python 3.6

from random import randint


class game:
    """game object to use as a counter"""

    def __init__(self, games=0, games_won=0, games_computer_won=0,
                 computer="", player=""):
        self.games = games
        self.games_won = games_won
        self.games_computer_won = games_computer_won
        self.computer = computer
        self.player = player

    def computer_choice(self):
        options = {1: "rock", 2: "paper", 3: "scissors"}
        self.computer = options[randint(1, 3)]

    def get_input(self, prompt):
        while True:
            print("\nEnter rock, paper, or scissors")
            choice = input(prompt)
            if choice.lower() in ("rock", "paper", "scissors"):
                self.player = choice.lower()
                break
            else:
                continue

    def player_won(self):
        self.games_won += 1

    def computer_won(self):
        self.games_computer_won += 1

    def __str__(self):
        return "\nYou won: {}, I won: {}".format(
            self.games_won, self.games_computer_won)


def main():
    # Initializes object to count games, games won, and player choices
    games = game(number_of_games())

    while games.games > 0:
        games.computer_choice()
        games.get_input(">  ")
        output(games, game_eval(games.computer, games.player))
        games.games -= 1
    print(games)


def number_of_games():
    while True:
        try:
            return int(input("Enter number of games to be played:  "))
            break
        except ValueError:
            print("ERROR: games must be integers only")
            continue


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


def output(games, win=None):
    if win == False:
        print("\nYou lost! ", end="")
        games.computer_won()
    elif win == True:
        print("\nYou won! ", end="")
        games.player_won()
    else:
        print("\nOoh, it's a tie! ", end="")
    print("computer: {}, player: {}".format(games.computer, games.player))


main()
