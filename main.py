from player import Player
from slot_machine import SlotMachine

def play_slot_machine():
    player = Player(balance=100)
    slot_machine = SlotMachine()

    while player.balance > 0:
        bet_amount = int(input(f"Your balance: {player.balance}. Enter your bet: "))
        if player.bet(bet_amount):
            spin_result = slot_machine.spin()
            payout = slot_machine.display(spin_result)
            player.win(payout)
        else:
            print("Game over. You don't have enough balance to continue.")
            break

if __name__ == "__main__":
    play_slot_machine()

