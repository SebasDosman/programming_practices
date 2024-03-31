def __bucketSort__(list): 
    maxValue = max(list)
    size = maxValue / len(list)
    
    cubeList = [] 
    
    for x in range(len(list)):
        cubeList.append([])
    
    for i in range(len(list)): 
        j = int (list[i] / size) 
        
        if (j != len(list)): 
            cubeList[j].append(list[i]) 
        else: 
            cubeList[len(list) - 1].append(list[i]) 
    
    for z in range(len(list)): 
        __insertionSort__(cubeList[z])
    
    listFinal = [] 
    
    for x in range(len(list)): 
        listFinal = listFinal + cubeList[x] 
    
    return listFinal

def __insertionSort__(list):
    for i in range(1, len(list) + 1):
        k = i - 1
        
        while (k > 0) and (list[k] < list[k - 1]):
            list[k], list[k - 1] = list[k - 1], list[k]
            k -= 1

newList = [29, 25, 3, 49, 9, 21, 43]
__bucketSort__(newList)