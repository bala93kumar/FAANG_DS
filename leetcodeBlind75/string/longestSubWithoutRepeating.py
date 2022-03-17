
# def longestSubwithoutRepeating(arr):
#
#     charset =  set()
#     l  =  0
#     max_val  = 0
#
#     for i in range(len(arr)):
#         while arr[i] in charset:
#             charset.remove(arr[i])
#             l +=1
#         charset.add(arr[i])
#         max_val  = max(max_val , i-l+1)
#
#     return max_val

def optimized(arr):

    map = dict()
    start = 0
    max_val =  0

    for i in range(len(arr)):
        if arr[i] in map :
            start = map[arr[i]] +1
        else :
            max_val = max(max_val , i-start +1)
        map[arr[i]] = i

    return max_val


if __name__ == "__main__":

    str1 =  "abcabcbb"
    str2 ="pwwkew"
    str3 = "bbbbb"
    # print(longestSubwithoutRepeating(str1))
    print(optimized(str3))

