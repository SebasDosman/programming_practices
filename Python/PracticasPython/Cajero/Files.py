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

    def write_file_consignment(self, consignment : array):
        try:
            with open(self.path, "a") as file:
                file.write("Consignment (" + ("".join(str(consignment))) + ") \n")
        except OSError:
            print("File not found")
        finally:
            file.close()