from array import array
from Cashier import Cashier

class Files(object):
    def __init__(self, path_write : str, path_read : str):
        self.path_write = path_write
        self.path_read = path_read
    
    def write_file_withdrawal(self, withdrawal : array):
        try:
            with open(self.path_write, "a") as file:
                file.write("Withdrawal (" + ("".join(str(withdrawal))) + ") \n")
        except FileNotFoundError:
            print("File not found")
            exit()
        finally:
            file.close()	

    def write_file_consignment(self, consignment : array):
        try:
            with open(self.path_write, "a") as file:
                file.write("Consignment (" + ("".join(str(consignment))) + ") \n")
        except FileNotFoundError:
            print("File not found")
            exit()
        finally:
            file.close()
    
    def execute_transactions(self, cashier : Cashier):
        try:
            with open(self.path_read, 'r') as file:
                for line in file:
                    if line.startswith('Inicio'):
                        values = [int(i.strip()) for i in line.split('(')[1].split(')')[0].split(',')]
                        cashier.start(values)
                        
                        print("-----------------------")
                        print("Start: ", cashier.bills)
                        cashier.print_money()
                        print("-----------------------")
                    elif line.startswith('Consignacion'):
                        values = [int(i.strip()) for i in line.split('(')[1].split(')')[0].split(',')]
                        cashier.consignment(values)
                        
                        print("-----------------------")
                        print("Consignment: ", cashier.bills)
                        cashier.print_money()
                        print("-----------------------")
                    elif line.startswith('Retiro'):
                        values = int(line.split('(')[1].split(')')[0])
                        value = cashier.withdrawal(values)
                        
                        print("-----------------------")
                        print("Withdrawal: ", value)
                        cashier.print_withdrawal(value)
                        print("-----------------------")
        except FileNotFoundError:
            print("File not found")
            exit()
            
        return [cashier.total(), cashier.total_withdrawn, cashier.total_consignment, cashier.total_invalid_withdrawal]