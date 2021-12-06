

def bs(arr, value):

    strt = 0
    end = len(arr)-1


    while end >=  strt:

        mid = round((strt + end) / 2)

        if arr[mid] == value:
            return print("Value found  at {}".format(mid))

        elif  value < arr[mid]:
            end =  mid  - 1

        elif value > arr[mid]:
            strt = mid + 1

    return -1

if __name__== "__main__":

    list1 = [2,5,8,13,15,20,25]

    bs(list1,8)

