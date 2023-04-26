class Rooms(object):
    room_number = 0
    location = ""

    def __init__(self, room_number : int, location : str):
        self.room_number = room_number
        self.location = location