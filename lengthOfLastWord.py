import  sys


def lengthOfWord(string):

    count  = 0
    n = len(string)
    print(n)
    i = 0

    for i in range(0, n):
        if string[i] == ' ':
            count += 1

    count += 1
    print('the number of words is : {0}'.format(count))
if __name__  == '__main__':
    print('bala')

    string_input  = input()

    print(string_input)

    lengthOfWord(string_input)
