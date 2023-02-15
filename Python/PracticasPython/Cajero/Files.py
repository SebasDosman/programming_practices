from Cashier import Cashier
from array import array

class Files(object):
    def __init__(self, path : str):
        self.path = path
    
    def write_file_withdrawal(self, withdrawal : array):
        try:
            with open(self.path, "a") as file:
                file.write("Withdrawal (" + ("".join(str(withdrawal))) + ") \n")
        except FileNotFoundError:
            print("File not found")
        finally:
            file.close()	

    def write_file_consigment(self, consigment : array):
        try:
            with open(self.path, "a") as file:
                file.write("Consigment (" + ("".join(str(consigment))) + ") \n")
        except OSError:
            print("File not found")
        finally:
            file.close()