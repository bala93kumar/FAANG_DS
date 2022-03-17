
list1  = [0,3,0,1,8]
list2 = [0,1,7,0,9,3]
          # 3,0
          #   1 0 0
          #     i
          #       j
def moveZeroes(arr):
    i = 0
    j = 0
    n = len(arr)

    while ( j < n):
    # for i in range(len(arr)):
        if arr[j] == 0 :
            j += 1
        else :
          temp = arr[i]
          arr[i] = arr[j]
          arr[j] = temp
          i +=1
          j +=1
    return arr

print(moveZeroes(list2))


