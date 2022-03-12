

list1 = [7,1,5,3,6,4]


list2 =  [1,2,4]
def maxProfit(prices ) -> int:

    max_val = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):

            if prices[j] > prices[i]:
                result = prices[j] - prices[i]

                max_val = max(max_val, result)

    return max_val


def maxProfitOptimized(arr):

    max_val = float('-inf')
    l = 0
    r = 1

    while(r < len(arr)):

        if arr[r] > arr[l]:
            res = arr[r] - arr[l]
            max_val = max(max_val , res)
            r += 1
        else :
            l = r
            r += 1


    return max_val

print(maxProfit(list2))

# print(maxProfitOptimized(list2))
