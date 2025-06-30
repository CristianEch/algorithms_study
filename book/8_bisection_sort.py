def sort_recursive(array, n= 0):
    if len(array) <= 1:
        return array[:]
    else:
        pivot = array[0]
        less = [n for n in array if n < pivot]
        more = [n for n in array if n > pivot]
        return sort_recursive(more,n) + [pivot] + sort_recursive(less,n) 
    

print(sort_recursive([5,8,7,80,3,20]))
        


        


