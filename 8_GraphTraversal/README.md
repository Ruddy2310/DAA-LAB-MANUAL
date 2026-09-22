# 8. Graph Traversal — BFS and DFS

## Aim
To implement a graph using an adjacency list and perform searching using
**Breadth-First Search (BFS)** and **Depth-First Search (DFS)**.

## Theory
- **Graph**: A collection of vertices (nodes) connected by edges. Represented
  here using an **adjacency list**, which stores, for every vertex, a linked
  list of its neighboring vertices.
- **BFS (Breadth-First Search)**: Explores the graph level by level using a
  **Queue**. Starts at a source vertex, visits all its neighbors first, then
  moves to the next level of neighbors.
- **DFS (Depth-First Search)**: Explores as far as possible along each branch
  before backtracking, implemented using **recursion** (implicit stack).

## Complexity
| Algorithm | Time Complexity | Space Complexity |
|-----------|-----------------|-------------------|
| BFS       | O(V + E)        | O(V)              |
| DFS       | O(V + E)        | O(V)              |

Where `V` = number of vertices, `E` = number of edges.

## Files
- `graph_traversal.c` — menu-driven C program: build graph, display adjacency
  list, run BFS, run DFS.

## How to Compile & Run
```bash
gcc graph_traversal.c -o graph_traversal
./graph_traversal
```

## Sample Input/Output
```
Vertices: 6
Edges: 7
Edge list: 0 1, 0 2, 1 3, 1 4, 2 4, 3 5, 4 5

BFS from vertex 0: 0 2 1 4 3 5
DFS from vertex 0: 0 2 4 5 3 1
```
(Traversal order depends on edge-insertion sequence in the adjacency list.)
