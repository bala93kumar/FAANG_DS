
from collections import deque


def removeDup(word, k):
    stack = deque()
    # stack.append(("bala",1))

    for i in range(0,len(word)):
        if len(stack) == 0:
            stack.append([word[i],1])
        elif stack[-1][0] == word[i] and stack[-1] and stack[-1][1] < k:
            stack[-1][1]+=1
            if stack[-1][1] == k :
                stack.pop()
        else :
            stack.append([word[i],1])
    res  = ''
    for value , count in stack:
        res+= value*count
    return res




if __name__ == "__main__":
    text = "pbbcggttciiippooaais"

    print(removeDup(text,2))