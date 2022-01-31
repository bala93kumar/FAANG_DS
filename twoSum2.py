

def twoSumTwo(nums , target ):

    l = 0
    r = len(nums) -1
    while l< r:
        curSum  =  nums[l] + nums[r]
        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        else :
            return [l+1 , r+1]
    return []


def bruteForce(nums,target):

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            sum = nums[i] + nums[j]
            if target == sum:
                return [i,j]


if __name__ == "__main__":

    arr =  [2, 6, 5, 8 ,11]

    target = 11

    # print(twoSumTwo(arr, 11))

    print(bruteForce(arr,target))