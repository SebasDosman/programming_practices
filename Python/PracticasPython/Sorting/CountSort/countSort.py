def __countSort__(list, index):
    countList = [0] * (index + 1)
    print(countList)
    orderList = [None] * len(list)
    print(orderList)
    
    for i in list:
        countList[i] += 1
    
    total = 0
    
    print(countList)
    for i in range(len(countList)):
        countList[i], total = total, total + countList[i]
    print(countList)
    
    for index in list:
        orderList[countList[index]] = index
        countList[index] += 1
    print(orderList)
    
    return orderList

oddList = [9, 3, 1, 5, 9, 2, 0, 1]
__countSort__(oddList, max(oddList))
