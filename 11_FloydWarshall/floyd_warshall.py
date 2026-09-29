INF = float("inf")

def floyd_warshall(dist):
    n = len(dist)
    d = [row[:] for row in dist]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    return d

def print_matrix(m):
    for row in m:
        print(" ".join("INF" if x == INF else f"{x:3}" for x in row))

if __name__ == "__main__":
    graph = [
        [0,   3,   INF, 7],
        [8,   0,   2,   INF],
        [5,   INF, 0,   1],
        [2,   INF, INF, 0],
    ]
    print("Input matrix:")
    print_matrix(graph)
    result = floyd_warshall(graph)
    print("\nAll-pairs shortest distances:")
    print_matrix(result)
