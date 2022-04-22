# Floyd warshall Algorithm implementation
def floyd_warshall(arr, v):

    # Adding vertices individually
    for k in range(v):
        for i in range(v):
            for j in range(v):
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
    # Printing the solution
    for i in range(v):
        for j in range(v):
            print(arr[i][j], end="  ")
        print(" ")


INF = 999
G = [[0, 3, INF, 5],
     [2, 0, INF, 4],
     [INF, 1, 0, INF],
     [INF, INF, 2, 0]]
V = 4
floyd_warshall(G, V)
