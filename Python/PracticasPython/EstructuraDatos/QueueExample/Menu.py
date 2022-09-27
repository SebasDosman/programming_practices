from User import User
from QueueClass import Queue

class Menu(object):
    def __welcomeMessage__():
        print("Welcome to Global - Moving S.A")
    
    def __menu__():
        print("\n Menu: \n", 
              "1. Add users to queue \n",
              "2. Quit user to queue \n",
              "3. Create the list of users with successful and pending request \n",
              "4. Print the report")
        
        option = int(input("Type an option: "))
        return option
    
    def __printRequirements__(usersQueue : Queue, usersListSuccessful : User, usersListPending :  User):
        print("\n Queue Length: ", usersQueue.length)
        print("Users with successful request: ")
        for i in range(0, len(usersListSuccessful)):
            usersListSuccessful[i].__toString__()
        print("Users with pending successful: ")
        for i in range(0, len(usersListPending)):
            usersListPending[i].__toString__()
    
    def __goodBye__():
        print("\n Thanks for use the software")