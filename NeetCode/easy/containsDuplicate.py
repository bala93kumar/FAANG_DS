list1 = [1,2,3,1]

def ifDup(arr):

    hset = set()

    for i  in arr:
        if i in hset:
            return False
        else :
            hset.add(i)
    return True


print(ifDup(list1))

