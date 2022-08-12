# <-- Bubble Sort -->

def __bubbleSort__(list):
    for i in range(0, len(list) - 1):
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                
                print(list)

oddList = [51, 7, 33, 13, 79, 21]

# __bubbleSort__(oddList)


# <-- Bubble Sort Better -->

def __bubbleSortBetter__(list):
    i = 0
    control = True
    
    while (i <= len(list) - 2 and control):
        control = False
        
        for j in range(0, len(list) - i - 1):
            if (list[j] > list[j + 1]):
                list[i], list[j + 1] = list[j + 1], list[j]
                
                control = True
                
                print(list)
            i += 1

oddList = [13, 3, 23, 43, 93, 73]

__bubbleSortBetter__(oddList)