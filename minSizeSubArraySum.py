

def minSubArray(nums,target):

    l = 0
    total_len = float("inf")
    total = 0

    for i in range(len(nums)):
        total += nums[i]

        while total >= target:
            length = i - l + 1
            total_len =  min(total_len, length)
            total -= nums[l]
            l+= 1

    return 0 if total_len == float("inf") else  total_len

if __name__ == "__main__":

    arr = [2,3,1,2,4,3]

    print(minSubArray(arr,7))