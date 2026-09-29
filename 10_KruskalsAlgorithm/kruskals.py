class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True

def kruskals(n, edges):
    edges = sorted(edges, key=lambda e: e[2])
    ds = DisjointSet(n)
    mst, total = [], 0
    for u, v, w in edges:
        if ds.union(u, v):
            mst.append((u, v, w))
            total += w
    return mst, total

if __name__ == "__main__":
    n = 5
    edges = [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8),
             (1, 4, 5), (2, 4, 7), (3, 4, 9)]
    mst, total = kruskals(n, edges)
    print("Edges in MST (u - v : weight):")
    for u, v, w in mst:
        print(f"{u} - {v} : {w}")
    print("Total weight of MST:", total)
