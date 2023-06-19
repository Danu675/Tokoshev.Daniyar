git init
pip install python-decouple
pip freeze > requirements.txtgi
from game_logic import play_game

if __name__ == "__main__":
    play_game()
from win_loss_logic import check_win_loss
from decouple import config

def play_game():
    slots = list(range(1, 31))
    money = float(config("MY_MONEY"))
    playing = True

    while playing:
        bet = input("Enter your bet amount: ")
        selected_slot = int(input("Enter the slot number you want to bet on: "))

        win = check_win_loss(selected_slot)

        if win:
            money += 2 * float(bet)
            print("Congratulations! You won.")
        else:
            money -= float(bet)
            print("Sorry! You lost.")

        print(f"Current money: {money}$")

        choice = input("Do you want to play again? (y/n): ")

        if choice.lower() != "y":
            playing = False

    print("Game over. Final result:")
    if money > float(config("MY_MONEY")):
        print("You won!")
    elif money == float(config("MY_MONEY")):
        print("It's a tie!")
    else:
        print("You lost!")

import random

def check_win_loss(selected_slot):
    winning_slot = random.randint(1, 30)
    return selected_slot == winning_slot
[DEFAULT]
MY_MONEY=1000

