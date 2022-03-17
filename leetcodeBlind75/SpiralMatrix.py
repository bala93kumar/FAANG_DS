


def spiralMatrix(matrix):

    top  = 0
    bottom = len(matrix) -1
    left = 0
    right  =  len(matrix[0]) -1


    while True:

        #print left to right
        if left > right :
            break

        for i in range(left , right+1):
            val1 = matrix[left][i]
            print(matrix[left][i], end=" ")

        top += 1
        if top > bottom:
            break

        for j in range(top ,bottom+1):
            val2 = matrix[j][right]
            print(matrix[j][right], end=" ")

        right -=1

        if  left > right :
            break
        for k in range(right , left -1 , -1):
            val3 = matrix[bottom][k]
            print(matrix[bottom][k],end=" ")

        bottom -=1

        #bottom to top

        if top > bottom:
            break
        for l in range(bottom ,top-1 , -1 ):
            val4 = matrix[l][left]
            print(matrix[l][left], end=" ")

        left +=1






if __name__ == "__main__":
    mat1 = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18] ]

    spiralMatrix(mat1 )

