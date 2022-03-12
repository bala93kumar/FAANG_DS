

list1 = [1,2,3,1,5,5]


def ifDup(arr):

    hashSet =  set()

    for i in arr:
        if i in hashSet:
            return True
        else :
            hashSet.add(i)
    return False

print(ifDup(list1))
