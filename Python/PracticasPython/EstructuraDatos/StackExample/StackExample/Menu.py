class Menu(object):
    def __welcomeMessage__(): 
        print("Welcome to Books - Knowledge S.A")
    
    def __menu__():
        print("\n Menu: \n",
              "1. Take out book from stack \n",
              "2. Sort list \n",
              "3. Print the report")
        
        option = int(input("Type an option: "))
        return option
    
    def __menuSort__():
        print("\n How do you want to sort the list? \n"
              "1. Year of launching \n",
              "2. Lexicography sort")
        
        option = int(input("Type an option: "))
        return option
    
    def __printRequirements__(bookList):
        print("\n Users with successful request: ")
        for i in range(0, len(bookList)):
            bookList[i].__toString__()
    
    def __goodBye__():
        print("\n Thanks for using the software")