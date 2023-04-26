from VendingMachine import VendingMachine
from Menu import Menu
from User import User
from File import File

menu = Menu(VendingMachine(), User(name = "Juan", admin = False), File("__configuration__/ConfiguracionExercise.txt"))
menu.run()