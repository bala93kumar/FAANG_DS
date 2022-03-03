
def isAnagram(s1,s2):

    if len(s1) != len(s2):
        return False
    count1 , count2 = {} , {}

    for i in range(len(s1)):

        count1[s1[i]] = 1 + count1.get(s1[i],0)
        # count2[s1[i]] = 1 + count2.get(s2[i],0)

    for i in range(len(s2)):
        count2[s2[i]] = 1 + count2.get(s2[i], 0)

    print(count1)
    print(count2)
    for i in count1:
        print(i,": ", count1[i])

        print(i, ":", count2[i])

        if count1[i] == count2.get(i,0):
            return True
        else :
            return False



s = 'anagram'
t = 'nagaram'

print(isAnagram(s,t))
