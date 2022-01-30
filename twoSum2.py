

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





if __name__ == "__main__":

    arr =  [2, 6, 5, 8 ,11]

    target = 9

    print(twoSumTwo(arr, 11))