
class QueensProblem:

    def __init__(self,n):
        self.n = n
        self.chess_table =  [[None for i in range(n)] for j in range(n)]

    def print(self):
        # return self.chess_table

        for i in range(self.n):
            for j in range(self.n):
                if self.chess_table[i][j] == 1:
                    print('Q',end=" ")
                else :
                    print('-', end =" ")
            print("\n")

    def returnResults(self):

        if self.solve(0):
            self.print()
        else:
            print("there is no solution")

    def solve_n_queens(self, col_index):

        if  col_index == self.n:
            return  True

        #lets try to find postiton for queen (col_index)
        for row_index in range(self.n):

            if self.isPlaceValid(row_index , col_index):
                self.chess_table[row_index][col_index] = 1

                if self.solve(col_index+1):
                    return True

                #backTrack
                self.chess_table[row_index][col_index] =0
        return False

    def isPlaceValid(self, row, col):
        #check the row if given queen can attack each other
        for i in range(self.n):
            if self.chess_table[row][i] == 1:
                return False




if __name__ == "__main__":

    chess = QueensProblem(3)
    print(chess.print())
    chess.returnResults()
