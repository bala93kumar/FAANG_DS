
#not working
def findMaxProblity(arr):

    for i in range(1,len(arr)):

        if i == 1 :
            arr[i] =  max(arr[i], arr[i-1])
        else:
            arr[i] = max(arr[i-2]+ arr[i], arr[i-1])


    arr[i]  = max(arr[i]+arr[i-2], arr[i-1])

    return arr[len(arr)-1]

if __name__ == "__main__":

    list1 =  [1,2,3,1]

    print(findMaxProblity(list1))
