from array import array
from Cashier import Cashier

class Files(object):
    def __init__(self, path : str):
        self.path = path
    
    def write_file_withdrawal(self, withdrawal : array):
        try:
            with open(self.path, "a") as file:
                file.write("Withdrawal (" + ("".join(str(withdrawal))) + ") \n")
        except FileNotFoundError:
            print("File not found")
            exit()
        finally:
            file.close()	

    def write_file_consignment(self, consignment : array):
        try:
            with open(self.path, "a") as file:
                file.write("Consignment (" + ("".join(str(consignment))) + ") \n")
        except FileNotFoundError:
            print("File not found")
            exit()
        finally:
            file.close()
    
    def execute_transactions(self, cashier : Cashier):
        try:
            with open(self.path, 'r') as file:
                for line in file:
                    if line.startswith('Inicio'):
                        values = [int(i.strip()) for i in line.split('(')[1].split(')')[0].split(',')]
                        cashier.start(values)
                        cashier.print_money()
                    elif line.startswith('Consignación'):
                        values = [int(i.strip()) for i in line.split('(')[1].split(')')[0].split(',')]
                        cashier.consignment(values)
                        cashier.print_money()
                    elif line.startswith('Retiro'):
                        values = int(line.split('(')[1].split(')')[0])
                        cashier.print_withdrawal(cashier.withdrawal(values))
        except FileNotFoundError:
            print("File not found")
            exit()
            
        return cashier