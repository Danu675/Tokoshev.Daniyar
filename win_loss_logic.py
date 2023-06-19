import random

def check_win_loss(selected_slot):
    winning_slot = random.randint(1, 30)
    return selected_slot == winning_slot
