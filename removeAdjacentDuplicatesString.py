
from collections import deque

def duplicateRemoval(word):

    stack = deque()

    for i in range(0,len(word)):
        if len(stack) == 0 :
            stack.append(word[i])
        elif stack[-1] == word[i]:
            stack.pop()
        else:
            stack.append(word[i])

    return stack

if __name__ == "__main__":

    word = input()
    print(duplicateRemoval(word))