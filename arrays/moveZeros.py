


list1 = [1,2,0,3,0,1]

def move_zeroes(arr):

    current_index = 0
    for i in range(len(list1)):
        if arr[i] != 0 :
            arr[current_index] = arr[i]
            current_index += 1
    print(current_index)
    return arr


def moveZeoresLeetcode(arr):

    n = len(arr)

    if n == 0 or n== 1:
        return -1

    left = 0
    right = 0

    while(right < n):
        if arr[right] == 0:
            right +=1
        else :
            temp  =  arr[left]
            arr[left] =  arr[right]
            arr[right] = temp
            left +=1
            right +=1
    return arr


# print(move_zeroes(list1))

print(moveZeoresLeetcode(list1))