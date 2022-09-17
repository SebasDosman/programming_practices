def __quickSort__(list, first, last):
    left = first
    right = last - 1
    pivot = last
    
    while (left < right):
        while (list[left] < list[pivot]) and (left <= right):
            left += 1
        
        while (list[right] > list[pivot]) and (right >= left):
            right -= 1
        
        if (left < right):
            list[left], list[right] = list[right], list[left]
            print(list)
        
    if (list[pivot] < list[left]):
            list[left], list[pivot] = list[pivot], list[left]
            print(list)
        
    if (first < left):
        __quickSort__(list, first, left - 1)
        
    if (last > left):
        __quickSort__(list, left + 1, last)

oddList = [11, 3, 81, 7, 45]
__quickSort__(oddList, 0, len(oddList) - 1)