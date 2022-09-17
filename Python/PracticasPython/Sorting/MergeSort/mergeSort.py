def __mergeSort__(list):
    if (len(list) <= 1):
        return list
    else:
        middle = len(list) // 2
        left = []
        
        for i in range(0, middle):
            left.append(list[i])
        
        right = []
        
        for i in range(middle, len(list)):
            right.append(list[i])
        
        left = __mergeSort__(left)
        right = __mergeSort__(right)
        
        if (left[middle - 1] <= right[0]):
            left += right
            return left
        
        result = __merge__(left, right)
        return result

def __merge__(left, right):
    newList = []
    
    while (len(left) > 0) and (len(right) > 0):
        if (left[0] < right[0]):
            newList.append(left.pop(0))
        else:
            newList.append(right.pop(0))
    
    if (len(left) > 0):
        newList += left
    
    if (len(right) > 0):
        newList += right
    
    print(newList)
    return newList

oddList = [11, 3, 81, 7, 45]
__mergeSort__(oddList)