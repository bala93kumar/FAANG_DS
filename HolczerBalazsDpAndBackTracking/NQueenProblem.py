
class QueensProblem:

    def __init__(self,n):
        self.n = n
        self.chess_table =  [[None for i in range(n)] for j in range(n)]

    def print(self):
        return self.chess_table

    def solveQueens(self):

        if self.solve():
            

if __name__ == "__main__":

    chess = QueensProblem(3)
    print(chess.print())
