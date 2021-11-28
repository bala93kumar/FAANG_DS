




def selectionSort(arr,n):


    for i in range(0, n):
        min_idx =  i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx  = j
        arr[i], arr[min_idx] = arr[min_idx],   arr[i]






if __name__ == "__main__":

    arr = [5,6,10,9,2]

    selectionSort(arr,5)

    print(arr)