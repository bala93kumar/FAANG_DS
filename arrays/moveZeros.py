


list1 = [1,2,0,3,0,1]

def move_zeroes(arr):

    current_index = 0
    for i in range(len(list1)):
        if arr[i] != 0 :
            arr[current_index] = arr[i]
            current_index += 1
    print(current_index)
    return arr

print(move_zeroes(list1))