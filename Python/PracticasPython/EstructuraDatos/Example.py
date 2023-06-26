fruits = []
fruits.append("Kiwi")
fruits.append("Apple")
fruits.append("Orange")
fruits.append("Banana")
print(fruits)

fruits.sort()
print(fruits)

fruits.pop(0)
print(fruits)

fruits.insert(0, "Kiwi")
print(fruits)

def pyramidSum(lower, upper, margin):
    blanks = " " * margin
    
    print(blanks, lower, upper)
    
    if lower > upper:
        print(blanks, 0)
        return 0
    else:
        result = lower + pyramidSum(lower + 1, upper, margin + 4)
        print(blanks, result)
        return result
    
pyramidSum(1, 5, 0)