class Guest(object):
    id = 0
    name = ""
    phone_number = 0
    address = ""
    room_number = 0

    def __init__(self, id : int, name : str, phone_number : int, address : str, room_number : str):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.room_number = room_number
    
    def check_in(self):
        return "Checking in"

    def check_out(self):
        return "Checking out" 

    def pay_bill(self):
        return "Paying bill"

    def order_food(self):
        return "Ordering food"

    def submit_feedback(self):
        return "Submitting feedback"
