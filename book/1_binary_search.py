array = list(range(1,256+1))



def return_index(array,goal):
    low = 0
    high = len(array)-1
    guess = 0
    n= 0 # for checking
    while goal != guess:
        n += 1
        medio = (high + low)//2  
        guess = array[medio] 
        print(f"{n}. *************{guess}")
        print(goal>guess)
        if goal > guess:
            print(f"{n} first if")
            low = medio + 1

        
        elif goal < guess:
            print(f"{n} second if")
            high = medio
        else:
            print(f"{n} else")
            return f" guess = {guess} equals to array[{medio}]"


print(return_index(array,256))

