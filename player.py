class Player:
    def __init__(self, balance=100):
        self.balance = balance
    
    def bet(self, amount):
        if amount > self.balance:
            print("Not enough balance!")
            return False
        self.balance -= amount
        return True
    
    def win(self, amount):
        self.balance += amount

