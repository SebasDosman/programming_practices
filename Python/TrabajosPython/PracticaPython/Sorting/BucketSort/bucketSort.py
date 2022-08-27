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
        insercion(cubeList[z])

    listFinal = [] 
    
    for x in range(len(list)): 
        listFinal = listFinal + cubeList[x] 
    
    return listFinal

newList = [29, 25, 3, 49, 9, 21, 43]
__bucketSort__(newList)
