from Cashier import Cashier
from Files import Files
from Reports import Reports

class Menu(object):
    def __init__(self, cashier_write : Cashier, cashier_read : Cashier, file1 : Files, file2 : Files, file3 : Files, report : Reports):
        self.cashier_write = cashier_write
        self.cashier_read = cashier_read
        self.file1 = file1
        self.file2 = file2
        self.file3 = file3
        self.report = report

    def __menu__(self):
        print("-----------------------")
        print("Menu")
        print("1. Consignment")
        print("2. Withdrawal")
        print("3. Denomination count")
        print("4. Total")
        print("5. Read files")
        print("6. Generate report")
        print("7. Exit")
        
        try:
            option = int(input("Choose an option: "))
        except ValueError:
            print("You must enter only numbers")
            
            Menu.__menu__(self)
        
        print("-----------------------")
        
        if option == 1:
            try:
                bills = [int(x) for x in input("Enter the bills: ").split()]
            except ValueError:
                print("You must enter only numbers")
                
                Menu.__menu__(self)
            
            self.cashier_write.consignment(bills)
            
            self.file1.write_file_consignment(self.cashier_write.bills)
            
            print("\n", self.cashier_write.denomination_count())
            self.cashier_write.print_money()
            
            Menu.__menu__(self)
        elif option == 2:
            try:
                amount = int(input("Enter the amount: "))
            except ValueError:
                print("You must enter only numbers")
                
                Menu.__menu__(self)
            
            withdrawal = self.cashier_write.withdrawal(amount)
            
            self.file1.write_file_withdrawal(self.cashier_write.withdrawn)
            
            print("\n", withdrawal)
            self.cashier_write.print_withdrawal(withdrawal)
            
            Menu.__menu__(self)
        elif option == 3:
            print("\n", self.cashier_write.denomination_count())
            self.cashier_write.print_money()
            
            Menu.__menu__(self)
        elif option == 4:
            print("Total: ", self.cashier_write.total())
            print("Withdrawal: ", self.cashier_write.total_withdrawn, "\n")
            
            self.cashier_write.print_money()
            
            Menu.__menu__(self)
        elif option == 5:
            return_list = self.file1.execute_transactions(self.cashier_read)
            print("Total: ", return_list[0])
            print("Total withdrawn: ", return_list[1])
            print("Total consignment: ", return_list[2])
            print("Total invalid withdrawal: ", return_list[3])
            
            Menu.__menu__(self)
        elif option == 6:
            self.cashier_read.reset()
            return_list1 = self.file1.execute_transactions(self.cashier_read)
            self.cashier_read.reset()
            return_list2 = self.file2.execute_transactions(self.cashier_read)
            self.cashier_read.reset()
            return_list3 = self.file3.execute_transactions(self.cashier_read)
            self.cashier_read.reset()
            
            self.report.generate_report(return_list1, return_list2, return_list3)
            
            Menu.__menu__(self)
        elif option == 7:
            print("Thanks for use the program! :D")
            
            exit()
        else:
            print("Invalid option")
            
            Menu.__menu__(self)