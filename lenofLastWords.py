
def lenOfLastWord(word):
    count = 0
    for i in range(0, len(word)):
        if word[i] != ' ':
            count += 1
        elif word[i] == ' ':
            count = 0
    return count


if __name__ == "__main__":

    print(lenOfLastWord("my name is  bala"))
