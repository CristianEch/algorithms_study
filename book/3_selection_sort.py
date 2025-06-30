from a_smallest import smallest_element_index

def sort_array(array):
    sorted_array = []

    while len(array) > 0:
        sorted_array.append(array.pop(smallest_element_index(array)))

    return sorted_array


arra = [3,20,5,13,1,9]
print(sort_array(arra))
