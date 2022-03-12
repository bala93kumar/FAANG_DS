list1 = [2,3,-2 , 4]

list2= [-2,0,-1]

def maxProductBruteForce(arr):
    max_val = 0
    for i in range(len(arr)):
        current_product = 1
        for j in range(i, len(arr)):
            current_product  *= arr[j]
            max_val = max(current_product, max_val)
            # max_val = max(max_val, current_product)

    return max_val


def  optimize(arr):

    cur_max = arr[0]
    cur_min = arr[0]

if __name__ == "__main__":


    print(maxProductBruteForce(list2))