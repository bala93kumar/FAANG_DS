
#Solutino is not working

def backTracck(n):
    r = n
    cols = set()
    posDiag = set()  # (r+c)
    nDiag = set()  # (r-c)

    res = []
    board = [['.'] * n for i in range(n)]


    if r == n :
        copy  = ["".join(row) for row  in board]
        res.append(copy)
        return res

    for c in range(n):
        if c in cols or (r+c) in posDiag or (r-c) in nDiag:
            continue

        cols.add(c)
        posDiag.add(r+c)
        nDiag.add(r-c)
        board[r][c] = "Q"

        backTracck(r+1)

        cols.remove(c)
        posDiag.remove(r+c)
        nDiag.remove(r-c)
        board[r][c] = "."

        return res


if __name__ == "__main__":

    print(backTracck(3))

