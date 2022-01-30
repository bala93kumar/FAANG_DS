


def twoSum(target , nums : list[int]):

    preMap = {}

    for i , n in enumerate(nums):
        diff = target - n
        if diff in preMap:
            return [i , preMap[diff]]
        preMap[n] = i
    return -1




if __name__ == "__main__":

    arr =  [2, 6, 5, 8 ,11]

    print(twoSum(14,arr))

    # premap1 = {1:2 , 2:3}
    #
    # print(premap1[1])





