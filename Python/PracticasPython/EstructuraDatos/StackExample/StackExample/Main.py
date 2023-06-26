from Data import book1, book2, book3, book4, book5, book6, book7, book8, book9, book10
from StackClass import Stack
from Menu import Menu
from Book import Book

bookList : Book = []

bookStack = Stack()
bookStack.__stack__(book1), bookStack.__stack__(book2), bookStack.__stack__(book3), bookStack.__stack__(book4), bookStack.__stack__(book5), bookStack.__stack__(book6), bookStack.__stack__(book7), bookStack.__stack__(book8), bookStack.__stack__(book9), bookStack.__stack__(book10)

Menu.__welcomeMessage__()
option1 = Menu.__menu__()

while (option1 != -1):
    if (option1 == 1):
        book = bookStack.__unstack__()
        bookList.append(book)
    elif (option1 == 2):
        option2 = Menu.__menuSort__()
        
        if (option2 == 1):
            bookListSort = sorted(bookList, key=lambda x : x.year, reverse=True) 
            bookList = bookListSort
        elif (option2 == 2):
            bookListSort = sorted(bookList, key=lambda x : x.name)
            bookList = bookListSort
    elif (option1 == 3):
        Menu.__printRequirements__(bookList)
    
    option1 = Menu.__menu__()

Menu.__goodBye__()