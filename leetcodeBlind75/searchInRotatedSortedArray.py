



list1 = [4,5,6,7,0,1,2]

def solution(arr,target):
    l = 0
    r =  len(arr) -1
    mid  =  (l+r) //2

    while l  <= r:

        if target == arr[mid]:
            return mid

        elif arr[mid] > target:
            l = mid + 1
        elif  mid < target:
            r  = mid - 1


print(solution(list1, 0))