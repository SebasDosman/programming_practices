

def __countingSort__(oddList, space):
    length = len(oddList)
    output = [0] * length
    count = [0] * 10
    
    for i in range(0, length):
        index = oddList [i] // space
        count[index % 10] += 1

    
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = length - 1

    while i >= 0:
        index = oddList[i] // space
        output[count[index % 10] - 1] = oddList [i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, length):
       oddList [i] = output[i]

def __radixSort__(oddList):
    max_element = max(oddList)
    space = 1

    while max_element // space > 0:
        __countingSort__(oddList, space)
        space *= 10

oddList = [11, 3, 81, 7, 45]
__radixSort__(oddList)
