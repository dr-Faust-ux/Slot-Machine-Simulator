import random

class SlotMachine:
    def __init__(self, reels=3, paylines=1, symbols=['🍒', '🍊', '🍋', '🍇', '🍉']):
        self.reels = reels
        self.paylines = paylines
        self.symbols = symbols
        self.payout_table = {'🍒': 5, '🍊': 3, '🍋': 2, '🍇': 4, '🍉': 10}
    
    def spin(self):
        return [random.choice(self.symbols) for _ in range(self.reels)]

    def check_payout(self, spin_result):
        payout = 0
        for symbol in spin_result:
            payout += self.payout_table.get(symbol, 0)
        return payout

    def display(self, spin_result):
        print(f"Spin result: {' | '.join(spin_result)}")
        payout = self.check_payout(spin_result)
        print(f"Payout: {payout}")
        return payout

