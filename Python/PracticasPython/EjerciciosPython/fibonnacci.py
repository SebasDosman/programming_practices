from array import array 

def fibonacci(n : int):
    if n <= 0:
        return [ ]
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = fibonacci(n - 1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

def list_comprehension(lista : array):
    return [int(array_index) for array_index in lista if array_index % 2 == 0]
    
def main(number : int):
    original_list = fibonacci(number)
    new_list = list_comprehension(original_list)

    print(original_list)
    print(new_list)