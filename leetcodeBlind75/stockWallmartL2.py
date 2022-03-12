

list1 = [12, 14, 13, 11, 10, 16, 20, 18, 15, 25, 24]


def bestTimeToSellStock(arr):
    result = len(arr) * [0]

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[i]:
                result[i] = (j - i)
                break
    return result


def optimized(arr):

    l = 0
    r = 1
    n = len(arr)

    result = len(arr) * [0]

    while(r < n):

        if arr[r] > arr[l]:

            result[l] = r - l
            r += 1
            l += 1
        else :
            r += 1

    return arr


# print(bestTimeToSellStock(list1))
print(optimized(list1))

