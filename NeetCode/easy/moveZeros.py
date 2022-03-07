iparr =   [0,2,0,3,0,12]

#move all zeroes to the right


def moveZeros(arr):
    l = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[l] , arr[i] = arr[i] , arr[l]
            l+= 1
    return arr

print(moveZeros(iparr))


