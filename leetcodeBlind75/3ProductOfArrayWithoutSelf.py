


list1  = [1,2,3,4]

#op  = [23,12,8,6]

#result array in prefix
#[1,1,2,6]

#result array in post fix
[24,12,8,6]

def arraySelfMultiply(arr):

    res = [1] * (len(arr))

    prefix = 1

    for i in range(len(arr)):
        res[i] = prefix
        prefix *= arr[i]

    postfix = 1
    for i in range(len(arr)-1 , -1 , -1):
        res[i] *= postfix
        postfix *= arr[i]

    return res

print(arraySelfMultiply(list1))


