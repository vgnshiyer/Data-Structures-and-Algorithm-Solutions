## 1.8 zero matrix

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

def zeroMatrix():
    nrows = len(matrix)
    ncols = len(matrix[0])
    rowzero = False
    colzero = False
    
    for i in range(ncols):
        if matrix[0][i] == 0:
            rowzero = True
            break
        
    for j in range(nrows):
        if matrix[j][0] == 0:
            colzero = True
            break
            
    for i in range(1, nrows):
        for j in range(1, ncols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    def makeRowZero(idx):
        for i in range(ncols):
            matrix[idx][i] = 0
            
    def makeColZero(idx):
        for i in range(nrows):
            matrix[i][idx] = 0
    
    ## cols
    for i in range(1, nrows):
        if matrix[i][0] == 0:
            makeRowZero(i)
            
    ## rows
    for i in range(1, ncols):
        if matrix[0][i] == 0:
            makeColZero(i)
            
    if(rowzero):
        makeRowZero(0)
        
    if(colzero):
        makeColZero(0)

def printMatrix():
    for row in matrix:
        print(row)
    print()

if __name__ == '__main__':
    printMatrix()
    zeroMatrix()
    printMatrix()
