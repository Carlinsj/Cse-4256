def identity(n):
    matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    rmatrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 1

    return matrix

def every_other_column(m, n):
    matrix = [[0 for _ in range(n)] for _ in range(m)]
    num = 1
    for j in range(0, n, 2):  
        for i in range(m):  
            matrix[i][j] = num
            num += 1
    return matrix

import numpy as np
def identity(n):
    return np.eye(n)



