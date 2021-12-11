

def find_dup(arr):

    count = 1

    for i in range(1,len(arr)):

        res1 = arr[i]
        res2 = arr[count-1]
        if arr[i] == arr[count-1]:
            continue

        arr[count] = arr[i]
        count += 1

    return count



if __name__ == "__main__":
    arr_1 = [0,0,1,1,1,2,2,3,3,4]

    print(find_dup(arr_1))

