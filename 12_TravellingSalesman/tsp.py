from itertools import permutations

def tsp_brute_force(dist, start=0):
    n = len(dist)
    cities = [i for i in range(n) if i != start]
    best_cost = float("inf")
    best_path = None
    for perm in permutations(cities):
        cost = 0
        cur = start
        for city in perm:
            cost += dist[cur][city]
            cur = city
        cost += dist[cur][start]
        if cost < best_cost:
            best_cost = cost
            best_path = (start,) + perm + (start,)
    return best_cost, best_path

if __name__ == "__main__":
    dist = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]
    cost, path = tsp_brute_force(dist)
    print("Minimum cost:", cost)
    print("Path:", " -> ".join(map(str, path)))
