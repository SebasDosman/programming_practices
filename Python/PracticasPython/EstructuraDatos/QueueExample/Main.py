from collections import UserList
from Menu import Menu
from QueueClass import Queue
from Data import user1, user2, user3, user4, user5, user6, user7, user8, user9, user10
from Request import Request

usersList = [user1, user2, user3, user4, user5, user6, user7, user8, user9, user10]
usersListSuccessful = []
usersListPending = []

usersQueue = Queue()
Menu.__welcomeMessage__()
option = Menu.__menu__()

while (option != -1):
    if (option == 1):
        usersQueue.__enqueue__(user1), usersQueue.__enqueue__(user2), usersQueue.__enqueue__(user3), usersQueue.__enqueue__(user4), usersQueue.__enqueue__(user5), usersQueue.__enqueue__(user6), usersQueue.__enqueue__(user7), usersQueue.__enqueue__(user8), usersQueue.__enqueue__(user9), usersQueue.__enqueue__(user10)
    elif (option == 2):
        usersQueue.__dequeue__()
    elif (option == 3):
        for i in range(0, len(usersList)):
            if (usersList[i].__getRequest__() == Request.SUCCESSFUL):
                usersListSuccessful.append(usersList[i])
            else:
                usersListPending.append(usersList[i])
    elif (option == 4):
        Menu.__printRequirements__(usersQueue, usersListSuccessful, usersListPending)
        usersListSuccessful = []
        usersListPending = []
    
    option = Menu.__menu__()

Menu.__goodBye__()