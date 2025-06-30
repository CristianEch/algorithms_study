def suma(array):
    if len(array) == 1: #base case
        return array[0]
    else:
        return array.pop() + sum(array) # recursive case
    

print(suma([1,2,3]))