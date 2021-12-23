
from itertools import combinations


def projectEstimate(arr :list[int], k):

    hashMap  = {}

    length = len(arr)

    for i in range(0 , length):
        value = arr[i]
        if value in hashMap:
            hashMap[value] += 1
        else :
            hashMap[value] = 1

    print(hashMap)

    count = 0
    for i in hashMap:
        value = i + k
        if value in hashMap:
            count += 1

    if count > 1:
        return count
    else:
        return -1


if __name__ == "__main__":

    input_1 =  [1,3,5,4,1]

    print(projectEstimate(input_1, 2))


