## 1.7 rotate matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]

def rotate():
    first, last = 0, len(matrix) - 1

    ## first and last governs the boundaries for the top, bottom, left, right layers
    ## we move to the other elements in the matrix using the offset which is the variable `i`
        
    while first < last: ## first and last are the boundaries
        for i in range(last - first): ## i is the offset
            top, bottom = first, last
            left, right = first, last
            
            # +/- i determines the part which can move
            topLeft = matrix[top][left + i]
            
            matrix[top][left + i] = matrix[bottom - i][left]
            
            matrix[bottom - i][left] = matrix[bottom][right - i]
            
            matrix[bottom][right - i] = matrix[top + i][right]
            
            matrix[top + i][right] = topLeft
        
        first += 1
        last -= 1    

def printMatrix():
    for row in matrix:
        print(row)
    print()

if __name__ == '__main__':
    printMatrix()
    rotate()
    printMatrix()