import random

def make_sudoku(size):
    if isinstance(size, int) and size > 0 and size <= 42:
        flagg = False
        while flagg == False:
            matrix = []
            x = 0
            rand = []
            count = 0

            for i in range(size**2):
                mat = []
                for r in range(1, size**2+1):
                    rand.append(r)

                for j in range(size**2):
                    flag = False
                    while flag == False:
                        x = random.choice(rand)
                        flag1 = False
                        for k in mat:
                            if k == x:
                                flag1 = True
                        flag2 = False
                        for l in range(i):
                            if x == matrix[l][j]:
                                flag2 = True
                        if flag1 == False and flag2 == False:
                            mat.append(x)
                            flag = True
                            for r in range(len(rand)):
                                if rand[r] == x:
                                    break
                            rand.pop(r)
                        count += 1
                        if count > 20:
                            mat.append(' ')
                            break

                matrix.append(mat)

            flagg = True
            for m in range(len(matrix)):
                for n in range(len(matrix[m])):
                    if matrix[m][n] == ' ':
                        flagg = False
                        break
                if flagg == False:
                    break

    return matrix


print (make_sudoku(1)) # [[1]]
print (make_sudoku(2)) # [[1,2,3,4],[3,4,1,2],[2,1,4,3],[4,3,2,1]]
print (make_sudoku(3)) # [[3,5,8,1,2,7,6,4,9],[6,7,4,5,8,9,3,2,1],[2,1,9,3,4,6,5,7,8],[9,8,6,7,1,4,2,5,3],[4,3,1,2,6,5,8,9,7],[7,2,5,9,3,8,1,6,4],[1,6,3,4,7,2,9,8,5],[8,9,7,6,5,1,4,3,2],[5,4,2,8,9,3,7,1,6]]

