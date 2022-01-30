
def lenOfLongSubStr(str):

    charSet = set()
    l = 0
    res = 0

    for r in range(len(str)):
        if str[r] in charSet:
            charSet.remove(str[l])
            l += 1
        charSet.add(str[r])
        res = max(res,r-l +1 )
    return res

if __name__ == "__main__":
    str = 'abcabcbb'
    print(lenOfLongSubStr(str))










