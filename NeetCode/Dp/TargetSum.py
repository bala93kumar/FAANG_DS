

#question

#  https://www.youtube.com/watch?v=g0npyaQtAQM&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&ab_channel=NeetCode

list1 = [1,1,1]



def findTarBf(arr, target):

    print("findTarget going 1st")

    def backTrack(i,total):

        print("i is {} & total is {}".format(i,total))

        if i == len(arr):
            return 1 if total == target  else 0

        return backTrack(i+1 , total + -arr[i]) + backTrack(i+1 , total + arr[i])

    return backTrack(0,0)


print(findTarBf(list1,1))


