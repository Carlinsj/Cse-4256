# Question 1
def star_m(n):

    if n <= 2:
        raise ValueError("n must be greater than 2")

    matrix = [[0] * n for _ in range(n)]
    
    for i in range(1, n):
        matrix[0][i] = 1
        matrix[i][0] = 1  # Symmetric connection
    
    return matrix

# Question 2
def star_d(n):
   
    if n <= 2:
        raise ValueError("n must be greater than 2")

    graph = {0: set(range(1, n))}  # Center node connected to all others
    for i in range(1, n):
        graph[i] = {0}  # Each outer node connects only to the center

    return graph

