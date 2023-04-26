class Bill(object):
    bill_number = 0
    guest_name = ""

    def __init__(self, bill_number : int, guest_name : str):
        self.bill_number = bill_number
        self.guest_name = guest_name