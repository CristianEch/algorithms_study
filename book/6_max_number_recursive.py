def max_number(array):
    if len(array) == 1:
        return array[0]
    elif len(array) == 2:
        if array[0] > array[1]:
            return array[0]
        else:
            return array[1]
    else:
        if array[0] > array[1]:
            array.pop(1)

            return max_number(array)
        else:
            array.pop(0)
            return max_number(array)
        
if __name__ == "__main__":
    print(max_number([5,13,100,8,61000]))