
#two sum of sorted array

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.


def twoSumOnSquare(arr,target):

    for i in range(len(arr)):
        find = target - arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] == find:
                return [i+1, j+1]


def twoSumOn(arr,target):

    left  = 0
    right = len(arr) - 1

    while (left < right):
        sum = arr[left] + arr[right]

        if sum == target:
            return [left+1, right+1]
        elif sum > target:
            right -= 1
        else :
            left +=1
    return -1





#solution in o(n)
list1 = [2,7,11,15]
# print(twoSumOnSquare(list1,9))

print(twoSumOn(list1,10))




