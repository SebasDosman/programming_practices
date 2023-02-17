from Cashier import Cashier
from Files import Files

files = Files("file.txt")

def __menu__(cashier : Cashier):
    print("-----------------------")
    print("Menu")
    print("1. Consignment")
    print("2. Withdrawal")
    print("3. Denomination count")
    print("4. Total")
    print("5. Exit")
    
    try:
        option = int(input("Choose an option: "))
    except ValueError:
        print("You must enter only numbers")
        exit()
    
    print("-----------------------")
    
    if option == 1:
        try:
            bills = [int(x) for x in input("Enter the bills: ").split()]
        except ValueError:
            print("You must enter only numbers")
            exit()
            
        cashier.consignment(bills)
        
        files.write_file_consignment(cashier.bills)
        
        print("\n", cashier.denomination_count())
        cashier.print_money()
        
        __menu__(cashier)
    elif option == 2:
        try:
            amount = int(input("Enter the amount: "))
        except ValueError:
            print("You must enter only numbers")
            exit()
        
        withdrawal = cashier.withdrawal(amount)
        
        files.write_file_withdrawal(cashier.withdrawn)
        
        print("\n", withdrawal)
        cashier.print_withdrawal(withdrawal)
        
        __menu__(cashier)
    elif option == 3:
        print("\n", cashier.denomination_count())
        cashier.print_money()
        
        __menu__(cashier)
    elif option == 4:
        print(cashier.total())
        cashier.print_money()
        
        __menu__(cashier)
    elif option == 5:
        print("Thanks for use the program! :D")
        
        exit()
    else:
        print("Invalid option")
        
        __menu__(cashier)