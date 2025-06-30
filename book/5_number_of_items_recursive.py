def num_items(array):
    if len(array) == 1:
        return 1
    else:
        array.pop()
        return 1 + num_items(array)
    

if __name__ == "__main__":
    print(num_items([1,1,1,1,1,1,1,1,1,1,1,1]))
