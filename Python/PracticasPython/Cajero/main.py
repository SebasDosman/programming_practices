from Cashier import Cashier
from menu import __menu__

cashier = Cashier()
cashier_read = Cashier()
cashier.start([100, 100, 100, 100, 100, 100, 100])
cashier_read.start([100, 100, 100, 100, 100, 100, 100])
__menu__(cashier, cashier_read)