from Cashier import Cashier
from Files import Files

file = Files("./__files__/file.txt")
read_file = Files("./__bankfiles__/BancoPython2.txt")

def __menu__(cashier : Cashier, cashier_read : Cashier):
    print("-----------------------")
    print("Menu")
    print("1. Consignment")
    print("2. Withdrawal")
    print("3. Denomination count")
    print("4. Total")
    print("5. Read files")
    print("6. Exit")
    
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
        
        file.write_file_consignment(cashier.bills)
        
        print("\n", cashier.denomination_count())
        cashier.print_money()
        
        __menu__(cashier, cashier_read)
    elif option == 2:
        try:
            amount = int(input("Enter the amount: "))
        except ValueError:
            print("You must enter only numbers")
            exit()
        
        withdrawal = cashier.withdrawal(amount)
        
        file.write_file_withdrawal(cashier.withdrawn)
        
        print("\n", withdrawal)
        cashier.print_withdrawal(withdrawal)
        
        __menu__(cashier, cashier_read)
    elif option == 3:
        print("\n", cashier.denomination_count())
        cashier.print_money()
        
        __menu__(cashier, cashier_read)
    elif option == 4:
        print("Total: ", cashier.total())
        print("Withdrawal: ", cashier.total_withdrawn)
        cashier.print_money()
        
        __menu__(cashier, cashier_read)
    elif option == 5:
        cashier_read = read_file.execute_transactions(cashier_read)
        print(cashier_read.total())
    elif option == 6:
        print("Thanks for use the program! :D")
        
        exit()
    else:
        print("Invalid option")
        
        __menu__(cashier, cashier_read)