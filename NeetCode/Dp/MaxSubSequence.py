list1  = [1,2,4]

list2  = [10,9,2,5,3 ]

# print(result)
# for j in range(3,4):
#     print(j)


def maxSumSequence(arr):
    maxVal = 1
    result = [1] * len(list1)

    for i in range(1,len(arr)):
        for j in range(0,i):
            if arr[i] > arr[j]:
                result[i] = max(result[i], 1+ result[j])
                maxVal =  max(maxVal, result[i])

    return maxVal

print(maxSumSequence(list1))



