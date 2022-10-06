def __evaluateString__(string):
    list = []
    
    for i in string:
        if (i in "(["):
            list.insert(0, i)
        else:
            if (len(list) == 0):
                return "No"
            
            value = list.pop(0)
            # pop the top of list
            if (i == ")" and value != "("):
                return "No"
            elif (i == "]" and value != "["):
                return "No"
    
    if (len(list) > 0):
        return "No"
    return "Yes"

value = eval(input())
for i in range(value):
    print(__evaluateString__(input()))