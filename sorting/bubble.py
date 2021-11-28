




def bubble(arr):

    # for printing in reverse list
    # for i in range(len(arr)-1,-1,-1):
    #     print(arr[i])
    for k in range(len(arr)):
        swapped = False
        for i in range(len(arr)-1-k):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1]= temp
                swapped = True
        if swapped is False:
            break









if __name__ == "__main__":

    arr = [5,6,10,9,2]

    bubble(arr)

    print(arr)