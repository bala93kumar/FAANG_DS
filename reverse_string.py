

def reverseString(word):
    reversed = []
    strt = 0
    end = len(word) - 1

    while strt <= end:
        reversed.append(word[end])
        end -= 1

    print(reversed)


if __name__ == '__main__':
    reverseString('bala')
