

def spiral(matrix):

    sr = 0
    er = len(matrix)
    sc = 0
    ec = len(matrix[0])

    print(er , ec)

    for i in range(sc,ec):
        print(matrix[sr][i])
        #  print(sr,j)

    sr+= 1

    for i in range(sr,er):
        print(matrix[i][er-1])

    ec = ec -1

    for i in range(ec-1,sc-1,-1):
        print(matrix[er -1][i])

    er = er -1
    # print('end row')
    # print(er)
    for i in range(er-1,sr-1,-1):
        print(matrix[i][sc])

    sc = sc+1












if __name__ == "__main__":

    mat = [ [1,2,3], [4,5,6], [7,8,9] ]

    spiral(mat)

