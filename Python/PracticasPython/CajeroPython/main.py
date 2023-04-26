from Cashier import Cashier
from Menu import Menu
from Files import Files
from Reports import Reports

menu = Menu(cashier_write = Cashier(), 
            cashier_read = Cashier(), 
            file1 = Files("__files__/file.txt", "__bank_files__/BancoPython.txt"),
            file2 = Files("__files__/file.txt", "__bank_files__/BancoPython2.txt"),
            file3 = Files("__files__/file.txt", "__bank_files__/BancoPython3.txt"),
            report = Reports("__reports__/report.pdf"))
menu.__menu__()