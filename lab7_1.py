matrix = [[[1,2,3],[3,2,1]], [[8,3,0,1,2,3,4,8,1,2,3],[3,2,1,2,3,9,4,7,9,2,3],[7,6,0,1,3,5,2,3,4,1,1]], [[21]]]

def saddle_point(matrix):
    x = None
    y = None
    
    for i in range(len(matrix)):
        countX = 0
        for j in range(len(matrix[i])):
            if min(matrix[i]) == matrix[i][j]:
                countX = countX + 1
                x = j
        
        mat = []
        for k in range(len(matrix)):
            mat.append(matrix[k][x])
        
        countY = 0
        for k in range(len(mat)):
            if max(mat) == mat[k]:
                countY = countY + 1
                y = k

        if countX == 1 and countY == 1 and matrix[i][x] == mat[y]:
            return (y, x)
        
    return False

for i in range(len(matrix)):
    print(saddle_point(matrix[i]))