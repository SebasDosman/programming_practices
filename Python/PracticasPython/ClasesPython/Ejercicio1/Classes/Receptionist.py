class Receptionist(object):
    id = 0
    name = ""
    phone_number = 0
    location = ""

    def __init__(self, id : int, name : str, phone_number : int, location : str):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.location = location
    
    def check_room_availability(self):
        return "Checking room availability"

    def check_room(self):
        return "Checking room"

    def generate_bill(self):
        return "Generating bill"

    def accept_customer_feedback(self):
        return "Accepting customer feedback"