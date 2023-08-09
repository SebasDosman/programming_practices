from Product import Product

class VendingMachine(object):
    def __init__(self):
        self.denominations = [200, 100, 50, 20, 10, 5, 2, 1]
        self.money_machine = [100 for i in range(len(self.denominations))]
        self.money_inserted = [0 for i in range(len(self.denominations))]
        self.products = []
        self.total_sales = 0
    
    def reset_money_inserted(self):
        self.money_inserted = [0 for i in range(len(self.denominations))]
    
    def modify_denominations(self, denominations : list):
        self.denominations = denominations
        
        self.money_inserted = [0 for i in range(len(denominations))]
        
    def modify_money_machine(self, money_machine : list):
        self.money_machine = money_machine
        
        self.money_inserted = [0 for i in range(len(money_machine))]
    
    def add_product(self, code : str, name : str, price : int, quantity : int):
        for product in self.products:
            if (product.code == code or product.name == name):
                product.quantity += quantity
                
                return
        
        new_product = Product(code, name, price, quantity)
        self.products.append(new_product)
    
    def remove_product(self, code : str):
        for product in self.products:
            if (product.code == code):
                self.products.remove(product)
                
                return
        
        print("\n There is no product with that code")
    
    def report_products(self, condition : bool):
        total_value = 0
        
        print("\nProducts: ")
        
        for product in self.products:
            total_value += product.price * product.quantity
            print(f"{ product.code }. { product.name } : { product.quantity } units - { product.price } cents each")
        
        if condition:
            print(f"Total value: { total_value } cents")

    def report_denominations(self, condition : bool):
        total_value = 0
        
        print("\nDenominations: ")
        
        for i in range(len(self.denominations)):
            total_value = self.total_money_machine()
            print(f"{ self.denominations[i] } cents: { self.money_machine[i] }")
        
        if condition:
            print(f"Total value: { total_value } cents")

    def insert_money_list(self, money : list):
        for i in range(len(money)):
            self.money_inserted[i] += money[i]
        
        print(f"\nMoney inserted: { self.total_money_inserted() } cents")
    
    def select_product_with_code(self, code : str):
        for product in self.products:
            if (product.code == code):
                return product
        return 
    
    def select_product_with_name(self, name : str):
        for product in self.products:
            if (product.name == name):
                return product
        return 

    def select_quantity(self, product : Product, quantity : int):
        if (self.total_money_inserted() >= product.price * quantity):
            if (product.quantity >= quantity):
                return True
        return False

    def remove_money(self, money : int):
        withdrawal = [0 for i in range(len(self.denominations))]
        
        if (money > self.total_money_inserted()):
            print("There is not enough balance to make the withdrawal")
        else :
            for i in range(len(self.denominations)):
                while self.money_machine[i] > 0 and money >= self.denominations[i]:
                    withdrawal[i] += 1
                    self.money_machine[i] -= 1
                    money -= self.denominations[i]
            
        return [withdrawal, sum(withdrawal[i] * self.denominations[i] for i in range(len(self.denominations)))]

    def calculate_money(self, money : list):
        money_list = [0 for i in range(len(self.denominations))]
        
        for i in range(len(self.denominations)):
            while self.money_machine[i] > 0 and money >= self.denominations[i]:
                money_list[i] += 1
                money -= self.denominations[i]
        
        return money_list

    def total_money_inserted(self):
        return sum(self.money_inserted[i] * self.denominations[i] for i in range(len(self.denominations)))
    
    def total_money_machine(self):
        return sum(self.money_machine[i] * self.denominations[i] for i in range(len(self.denominations)))

    def buy_product(self, code : str, quantity : int, is_quick_purchase : bool):
        if (self.select_product_with_code(code) == None):
            print("\n There is no products")
        else:
            product = self.select_product_with_code(code)
        
            if (self.select_quantity(product, quantity)):
                product.quantity -= quantity
                self.total_sales += product.price * quantity
                change_to_return = (self.total_money_inserted() - (product.price * quantity))
                
                [list_to_return, total_to_return] = self.remove_money(change_to_return)
                
                print(f"List to return: { list_to_return }")
                print(f"Money to return: { total_to_return } cents")
            else:
                print("Not enough money inserted or not enough products in stock")
        
        if (not is_quick_purchase):
            self.reset_money_inserted()