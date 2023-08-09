from VendingMachine import VendingMachine
import re

class File(object):
    def __init__(self, path : str):
        self.path = path
    
    def read(self, vending_machine : VendingMachine):
        try:
            with open(self.path, 'r') as file:
                for line in file:
                    if line.startswith("Denominaciones") or line.startswith("ï»¿Dollars"):
                        self.execute_denominations(vending_machine, file)
                    elif line.startswith("products") or line.startswith("Products # Name-Price-Quantity"):
                        self.execute_products(vending_machine, file)
                    elif line.startswith("Quick Purchase # Basic Level Name - Quantity - Money"):
                        print("\nQuick basic purchase: ")
                        
                        self.execute_basic_purchase(vending_machine, file)
                    elif line.startswith("Quick Purchase 2 # Advanced Level Name - Quantity - Money"):
                        print("\nQuick advanced purchase: ")
                        
                        self.execute_advanced_purchase(vending_machine, file)
        except FileNotFoundError:
            print("File not found")
    
    def execute_denominations(self, vending_machine : VendingMachine, file):
        list1, list2 = [], []
                        
        for denom_str in file:
            if (denom_str.isspace()):
                break
            else:
                denom, count = denom_str.split(", ")
                
                list1.append(int(denom.strip()))
                list2.append(int(count.strip()))
        
        vending_machine.modify_denominations(list1)
        vending_machine.modify_money_machine(list2)
    
    def execute_products(self, vending_machine : VendingMachine, file):
        for product_str in file:
            if (product_str.isspace()):
                break
            else:
                name, price, quantity = product_str.strip().split(", ")
                
                code = len(vending_machine.products) + 1
                
                vending_machine.add_product(str(code), str(name), int(price), int(quantity))

    def execute_basic_purchase(self, vending_machine : VendingMachine, file):
        for purchase_str_basic in file:
            if (purchase_str_basic.isspace()):
                break
            else:
                name, quantity, money = purchase_str_basic.strip().split(", ")
                
                product = vending_machine.select_product_with_name(name)
                money_list = vending_machine.calculate_money(int(money))
                vending_machine.insert_money_list(money_list)
                
                vending_machine.buy_product(product.code, int(quantity), False)
    
    def execute_advanced_purchase(self, vending_machine : VendingMachine, file):
        products = []
    
        for line in file:
            match = re.match(r'^\((.*?)\s*;\s*(\d+)\)$', line.strip())
            
            if match:
                price = int(match.group(2))
                for product in match.group(1).split(";"):
                    name, quantity = product.strip().split(",")
                    products.append((name.strip(), int(quantity.strip()), price))
        
        for i in range(len(products)):
            product = vending_machine.select_product_with_name(products[i][0])
            money_list = vending_machine.calculate_money(int(products[i][2]))
            vending_machine.insert_money_list(money_list)
            
            vending_machine.buy_product(product.code, products[i][1], False)