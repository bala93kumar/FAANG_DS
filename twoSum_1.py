
def twoSum(nums : list[int], target):

    hashMap = {}
    for i in range(0, len(nums)):   
        result = target - arr[i]
        if  result in hashMap:
            return [i,hashMap[result]]
        hashMap[arr[i]] = i
    return -1




if __name__ == "__main__":

    arr = [1,3,3,4]
    target = 5

    result = twoSum(arr, target)

    print(result)

    # premap1 = {1:2 , 2:3}
    #
    # print(premap1[2])


