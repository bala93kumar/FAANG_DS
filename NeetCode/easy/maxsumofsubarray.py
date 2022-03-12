
def bruteForce(list1):

    max_sum  =  float('-inf')
    for i in range(len(list1)):
        print("for i value equals : {}".format(list1[i]))
        for j in range(i, len(list1)):
            print("--------------")
            sum = 0
            for k in range(i, j+1):
                sum += list1[k]
                print(sum)
        if sum > max_sum:
            max_sum = sum
    print("max_sum  is {}".format(max_sum))


def onsquare(list1):

    max_sum  =  float('-inf')
    for i in range(len(list1)):
        print("for i value equals : {}".format(list1[i]))
        sum = 0
        for j in range(i, len(list1)):
            print("--------------")
            sum += list1[j]
            print(sum)
        if sum > max_sum:
            max_sum = sum
    print("max_sum  is {}".format(max_sum))


    #kandane algorithm o(n)
    #logic to return max is understood yet to understand to find the range
def kandane(list1):
    curr_sum = 0
    max_so_far = list1[0]

    # st = 0
    # en =0
    # poi = 0

    for i in range(len(list1)):
        curr_sum = curr_sum +  list1[i]
        if max_so_far < curr_sum:
            max_so_far = curr_sum

        if curr_sum < 0:
            curr_sum = 0
    return max_so_far



if __name__ == "__main__":
    list1 = [1, 2, -3, 4]

    # bruteForce(list1)

    # onsquare(list1)

    print(kandane(list1))