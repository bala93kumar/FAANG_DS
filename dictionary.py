

dict1 = {1:2, 3:4,2:1,6:7}

# print(dict1[1])


def maxoccur(dict1):
    keys = list(dict1.keys())
    index = 0
    count = 0
    for i in range(len(keys)):
        # print(dict1[keys[i]])
        if dict1[keys[i]] > count:
            count =  dict1[keys[i]]
            index =  keys[i]
    # if dict1[i] > count
    return index

print( maxoccur(dict1))
