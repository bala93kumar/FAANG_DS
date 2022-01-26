from collections import deque

stk = deque()

str =  'hello'

for i in range(0,len(str)):
    # print(str[i])
    stk.append(str[i])

for i in range(0,len(stk)):
    print(stk.pop())

#without using extra space:

#use two pointers strt , end and then swap strt with end

def reverse_manual(str):

    strt = 0
    end = len(str) -1
    temp = ' '
    while(strt <=end):

        str[strt] = temp

        strt += 1
        end -= 1

print(reverse_manual('abcd'))

#cant perfomr string item assignment in python , hence go with stack
