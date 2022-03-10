iparr =   [0,2,0,3,0,12]

#move all zeroes to the right


def moveZeroes(arr):
    left = 0
    right = 0

    for i in range(len(arr)):

        if arr[i] ==  0:
            right +=1
        else :
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left += 1
            right += 1
    return arr


print(moveZeroes(iparr))


