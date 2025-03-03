def directed_to_undirected(di):
    n = len(di)
    undirected = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if di[i][j] == 1 or di[j][i] == 1:
                undirected[i][j] = 1
                undirected[j][i] = 1
    
    return undirected
