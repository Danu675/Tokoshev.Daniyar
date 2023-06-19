import random
from decouple import config
from win_loss_logic import check_win_loss

def play_game():
    slots = list(range(1, 31))
    money = float(config("MY_MONEY"))
    playing = True

    while playing:
        print(f"Current money: {money}$")
        bet = float(input("Enter your bet amount: "))
        selected_slot = int(input("Enter the slot number you want to bet on: "))

        win = check_win_loss(selected_slot)

        if win:
            money += 2 * bet
            print("Congratulations! You won.")
        else:
            money -= bet
            print("Sorry! You lost.")

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
