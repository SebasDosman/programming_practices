from array import array 

class Cashier:
    def __init__(self):
        self.denominations = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
        self.bills = [100 for i in range(len(self.denominations))]
        self.total_withdrawn = 0
        self.withdrawn = 0
    
    def start(self, bills : array):
        self.bills = bills

    def consignment(self, bills : array):
        for i in range(len(bills)):
            self.bills[i] += bills[i]

    def withdrawal(self, amount : int):
        withdrawal = [0 for i in range(len(self.denominations))]
        
        for i in range(len(self.denominations)):
            while self.bills[i] > 0 and amount >= self.denominations[i]:
                withdrawal[i] += 1
                self.bills[i] -= 1
                amount -= self.denominations[i]
        self.total_withdrawn += sum(self.denominations[i] * withdrawal[i] for i in range(len(self.denominations)))
        self.withdrawn = sum(self.denominations[i] * withdrawal[i] for i in range(len(self.denominations)))
        
        return withdrawal

    def denomination_count(self):
        return self.bills

    def total(self):
        deposited = sum(self.bills[i] * self.denominations[i] for i in range(len(self.denominations)))
        
        return deposited - self.total_withdrawn
    
    def print_money(self):
        for i in range(len(self.denominations)):
            print("Money: ", self.denominations[i], "- Quantity: ", self.bills[i])
    
    def print_withdrawal(self, withdrawal : array):
        for i in range(len(self.denominations)):
            print("Money: ", self.denominations[i], "- Quantity: ", withdrawal[i])