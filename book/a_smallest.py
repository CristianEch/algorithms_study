def smallest_number(array):
    small = array[0]
    for number in array:
        if number <= small:
            small = number
    return small





def smallest_element_index(array):
    small = array[0]
    small_index = 0
    for index in range(len(array)):
        if array[index] < small:
            small = array[index]
            small_index = index
    return small_index


if __name__ == "__main__":
    lista = [8,1,20,0,6,99,8,33,21,22,56,-111,3,22,-5]
    print(smallest_number(lista))
    print(smallest_element_index([5,8,20,3,10,1]))