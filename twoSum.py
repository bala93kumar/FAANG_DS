

def twoSumBruteForce(target , nums):

    for i in range(0, len(arr)):
        for j in range(0 , len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]

    return -1

def twoSum(target , nums):

    preMap = {}

    for i , n in enumerate(nums):
        diff = target - n
        if diff in preMap:
            return [i , preMap[diff]]
        preMap[n] = i
    return -1




if __name__ == "__main__":

    arr =  [2, 6, 5, 8 ,11]

    # print(twoSum(14,arr))

    print("brute force solution")

    print(twoSumBruteForce(20,arr))

    # premap1 = {1:2 , 2:3}
    #
    # print(premap1[1])





