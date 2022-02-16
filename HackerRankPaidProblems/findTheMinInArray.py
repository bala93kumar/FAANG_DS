def minValue(arr,k):

    strt = 0

    result = []

    min_array = []

    while strt < len(arr):

        if strt+k < len(arr):
            for i in range(strt,strt+k):
                result.append(arr[i])


        if len(result) >= k:
            result.sort()
            min_array.append(result[0])
        else :
            break

        strt += 1
        result = []

    min_array.sort()

    max  =  min_array[len(min_array)-1]

    return max


if __name__ == "__main__":

    arr = [1,2,3,1,2]
    #arr = [8,2,4]
    print(minValue(arr,1))


