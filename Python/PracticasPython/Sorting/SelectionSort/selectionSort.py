def __selectionSort__(list):
    for i in range(0, len(list) - 1):
        minimal = i
        for j in range(i + 1, len(list)):
            if(list[j] < list[minimal]):
                minimal = j    
        list[i], list[minimal] = list[minimal], list[i]
        print(list)

oddlist = [11, 3, 81, 7, 45]
__selectionSort__(oddlist)