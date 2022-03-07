



def maxInArr(arr , length):

    if length == 0 :
        return arr[0]


    return max(arr[length], maxInArr(arr , length -1) )



arr1 = [10,3,4,5,10,19]

length  = len(arr1) -1
print(maxInArr(arr1, length))
