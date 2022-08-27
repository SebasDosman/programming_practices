def shellSort(list):
    interval = len(list) // 2
    
    while interval > 0:
        for i in range(interval, len(list)):
            temp = list[i]
            j = i
            
            while j >= interval and list[j - interval] > temp:
                list[j] = list[j - interval]
                j -= interval
            list[j] = temp
        interval //= 2

oddList = [11, 3, 81, 7, 45, 10]
shellSort(oddList)