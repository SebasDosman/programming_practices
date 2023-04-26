from User import User
from VendingMachine import VendingMachine
from File import File

class Menu(object):
    def __init__(self, vending_machine : VendingMachine, user : User, file : File):
        self.title = "Menu: "
        self.optionsUser = ["Insert money", "See products", "Buy product", "Read file", "Admin menu", "Exit"]
        self.optionsAdmin = ["Modify denominations", "Add product", "Remove product", "See money", "See products", "User menu", "Exit"]
        self.vending_machine = vending_machine
        self.user = user
        self.file = file

    def display(self, options : list):
        print("\n" + self.title)
        
        for i in range(len(options)):
            print(f"{ i + 1 }. { options[i] }")
    
    def user_menu(self):
        while True:
            self.display(self.optionsUser)
            
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("You must enter only numbers")
                
                self.user_menu()
            
            if choice == 1:
                try:
                    money = [int(x) for x in input("\nEnter the money you want to insert: ").split()]
                except ValueError:
                    print("You must enter only numbers")
                    
                    self.user_menu()
                
                self.vending_machine.insert_money_list(money)
            elif choice == 2:
                self.vending_machine.report_products(self.user.admin)
            elif choice == 3:
                try:
                    code = input("\nEnter the code of the product you want to buy: ")
                    quantity = int(input("Enter the quantity of the product you want to buy: "))
                except ValueError:
                    print("You must enter only numbers")
                    
                    self.user_menu()
                
                self.vending_machine.buy_product(code, quantity)
            elif choice == 4:
                self.file.read(self.vending_machine)
            elif choice == 5:
                self.run()
            elif choice == 6:
                print("\nThanks for using our vending machine!")
                
                break
            else:
                print("\nInvalid choice")
    
    def admin_menu(self):
        while True:
            self.display(self.optionsAdmin)
            
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("You must enter only numbers")
                
                self.admin_menu()
            
            if choice == 1:
                try:
                    denominations = [int(x) for x in input("\nEnter the denominations you want to add: ").split()]
                except ValueError:
                    print("You must enter only numbers")
                    
                    self.admin_menu()
                
                self.vending_machine.modify_denominations(denominations)
            elif choice == 2:
                try:
                    code = input("\nEnter the code of the product you want to add: ")
                    name = input("Enter the name of the product you want to add: ")
                    price = int(input("Enter the price of the product you want to add: "))
                    quantity = int(input("Enter the quantity of the product you want to add: "))
                except ValueError:
                    print("You must enter a valid option")
                    
                    self.admin_menu()
                
                self.vending_machine.add_product(code, name, price, quantity)
            elif choice == 3:
                try:
                    code = input("\nEnter the code of the product you want to remove: ")
                except ValueError:
                    print("You must enter a valid option")
                    
                    self.admin_menu()
                
                self.vending_machine.remove_product(code)
            elif choice == 4:
                self.vending_machine.report_denominations(self.user.admin)
            elif choice == 5:
                self.vending_machine.report_products(self.user.admin)
            elif choice == 6:
                self.user_menu()
            elif choice == 7:
                print("\nThanks for using our vending machine!")
                
                break
            else:
                print("\nInvalid choice")
    
    def run(self):
        if self.user.admin:
            print(f"\nWelcome, admin '{ self.user.name }'")
            
            self.admin_menu()
        else:
            print(f"\nWelcome, user '{ self.user.name }'")
            
            self.user_menu()