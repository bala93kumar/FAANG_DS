

def isSequence(arr,i):

    if i  == len(arr) - 1 :
        return True
    return ( arr[i] == arr[i+1] -1 and isSequence(arr,i+1) )



arr1 =  [2,3,4,5,6]

i = 0
print(isSequence(arr1, i))