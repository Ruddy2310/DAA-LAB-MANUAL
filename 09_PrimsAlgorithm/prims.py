import heapq

def prims(graph, start=0):
    n = len(graph)
    visited = [False] * n
    mst = []
    total = 0
    pq = [(0, start, -1)]  # (weight, vertex, parent)
    while pq:
        w, u, parent = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        total += w
        if parent != -1:
            mst.append((parent, u, w))
        for v, wt in graph[u]:
            if not visited[v]:
                heapq.heappush(pq, (wt, v, u))
    return mst, total

if __name__ == "__main__":
    graph = {
        0: [(1, 2), (3, 6)],
        1: [(0, 2), (2, 3), (3, 8), (4, 5)],
        2: [(1, 3), (4, 7)],
        3: [(0, 6), (1, 8), (4, 9)],
        4: [(1, 5), (2, 7), (3, 9)],
    }
    mst, total = prims(graph)
    print("Edges in MST (u - v : weight):")
    for u, v, w in mst:
        print(f"{u} - {v} : {w}")
    print("Total weight of MST:", total)
