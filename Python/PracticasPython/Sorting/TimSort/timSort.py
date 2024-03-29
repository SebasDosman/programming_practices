

MINIMUM = 32

def __minRun__(n): 
    r = 0
    
    while n >= MINIMUM: 
        r |= n & 1
        n >>= 1
    return n + r 

def __insertionSort__(array, left, right): 
    for i in range(left + 1, right + 1):
        element = array[i]
        j = i-1
        
        while element < array[j] and j >= left :
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = element
    return array

def __merge__(array, l, m, r): 
    array_length1= m - l + 1
    array_length2 = r - m 
    left = []
    right = []
    
    for i in range(0, array_length1): 
        left.append(array[l + i]) 
    for i in range(0, array_length2): 
        right.append(array[m + 1 + i]) 
    
    i = 0
    j = 0
    k = l
    
    while j < array_length2 and  i < array_length1: 
        if left[i] <= right[j]: 
            array[k] = left[i] 
            i += 1
        else: 
            array[k] = right[j] 
            j += 1
            
        k += 1
        
    while i < array_length1: 
        array[k] = left[i] 
        k += 1
        i += 1
        
    while j < array_length2: 
        array[k] = right[j] 
        k += 1
        j += 1

def __timSort__(array): 
    n = len(array) 
    minrun = __minRun__(n) 
    
    for start in range(0, n, minrun): 
        end = min(start + minrun - 1, n - 1) 
        __insertionSort__(array, start, end) 
        
    size = minrun 
    
    while size < n: 
        for left in range(0, n, 2 * size): 
            mid = min(n - 1, left + size - 1) 
            right = min((left + 2 * size - 1), (n - 1)) 
            __merge__(array, left, mid, right) 
        size = 2 * size 

array = [100, 3, 44, 2, 11, 33, 1] 
__timSort__(array) 