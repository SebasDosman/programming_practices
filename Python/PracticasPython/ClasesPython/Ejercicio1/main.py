from Classes.Bill import Bill
from Classes.Chef import Chef
from Classes.FoodItems import FoodItems
from Classes.Guest import Guest
from Classes.HouseKeeping import HouseKeeping
from Classes.Inventory import Inventory
from Classes.Manager import Manager
from Classes.Receptionist import Receptionist
from Classes.Rooms import Rooms

bill = Bill(5, "Mauro")
chef = Chef(1, "Juan", "Kitchen")
food_items = FoodItems(1, "Pizza")
guest = Guest(1, "Carlos", 123456789, "Street 1", "Kitchen")
house_keeping = HouseKeeping(1, "Pablo", "Room 1")
inventory = Inventory("Plastic", "Available")
manager = Manager(1, "David", "Manager", "Street 1")
receptionist = Receptionist(1, "Diana", 123456789, "Street 1")
rooms = Rooms(1, "Room 1")

print("\n", bill.guest_name, 
      "\n", chef.name, 
      "\n", food_items.name, 
      "\n", guest.name, 
      "\n", house_keeping.name, 
      "\n", inventory.type, 
      "\n", manager.name, 
      "\n", receptionist.name, 
      "\n", rooms.location)