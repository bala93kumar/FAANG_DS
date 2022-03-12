
def smalled(nums:list[int],k):

    for i in range(len(nums)-1,-1,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

    return nums[k-1]

def largest(nums:list[int],k):

    for i in range(len(nums)-1,-1,-1):
        for j in range(i):
            if nums[j] < nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp


    return nums[k-1]


if __name__  == "__main__":

    ip =  [4,2,6,5,1,3]
    k = 3

    print(smalled(ip, k))

    print(largest(ip,k))