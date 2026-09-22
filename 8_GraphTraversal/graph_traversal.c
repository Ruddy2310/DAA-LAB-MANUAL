/*
 * Practical 8: Implementation of Graph and Searching (BFS and DFS)
 * -------------------------------------------------------------
 * Design and Analysis of Algorithms Lab
 *
 * Description:
 *   Represents a graph using an adjacency list and implements
 *   two fundamental graph traversal / searching techniques:
 *     1. Breadth-First Search (BFS)  - uses a Queue
 *     2. Depth-First Search  (DFS)   - uses recursion (Stack via call stack)
 *
 * Time Complexity : O(V + E)  for both BFS and DFS
 * Space Complexity: O(V)      for the visited array / queue / recursion stack
 */

#include <stdio.h>
#include <stdlib.h>

#define MAX 100

// ---------- Adjacency List Node ----------
typedef struct Node {
    int vertex;
    struct Node* next;
} Node;

Node* adjList[MAX];
int visited[MAX];
int totalVertices;

// ---------- Simple Queue for BFS ----------
int queueArr[MAX], front = -1, rear = -1;

void enqueue(int val) {
    if (rear == MAX - 1) return;
    if (front == -1) front = 0;
    queueArr[++rear] = val;
}

int dequeue() {
    if (front == -1 || front > rear) return -1;
    return queueArr[front++];
}

int isQueueEmpty() {
    return front == -1 || front > rear;
}

// ---------- Graph Construction ----------
Node* createNode(int v) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->vertex = v;
    newNode->next = NULL;
    return newNode;
}

// Adds an undirected edge between src and dest
void addEdge(int src, int dest) {
    Node* newNode = createNode(dest);
    newNode->next = adjList[src];
    adjList[src] = newNode;

    newNode = createNode(src);
    newNode->next = adjList[dest];
    adjList[dest] = newNode;
}

void initGraph(int vertices) {
    totalVertices = vertices;
    for (int i = 0; i < vertices; i++) {
        adjList[i] = NULL;
        visited[i] = 0;
    }
}

// ---------- Breadth-First Search ----------
void BFS(int startVertex) {
    for (int i = 0; i < totalVertices; i++)
        visited[i] = 0;

    front = rear = -1;
    visited[startVertex] = 1;
    enqueue(startVertex);

    printf("BFS Traversal starting from vertex %d:\n", startVertex);

    while (!isQueueEmpty()) {
        int current = dequeue();
        printf("%d ", current);

        Node* temp = adjList[current];
        while (temp != NULL) {
            if (!visited[temp->vertex]) {
                visited[temp->vertex] = 1;
                enqueue(temp->vertex);
            }
            temp = temp->next;
        }
    }
    printf("\n");
}

// ---------- Depth-First Search (Recursive) ----------
void DFSUtil(int vertex) {
    visited[vertex] = 1;
    printf("%d ", vertex);

    Node* temp = adjList[vertex];
    while (temp != NULL) {
        if (!visited[temp->vertex]) {
            DFSUtil(temp->vertex);
        }
        temp = temp->next;
    }
}

void DFS(int startVertex) {
    for (int i = 0; i < totalVertices; i++)
        visited[i] = 0;

    printf("DFS Traversal starting from vertex %d:\n", startVertex);
    DFSUtil(startVertex);
    printf("\n");
}

// ---------- Utility: Display Adjacency List ----------
void displayGraph() {
    printf("\nAdjacency List Representation:\n");
    for (int i = 0; i < totalVertices; i++) {
        printf("Vertex %d: ", i);
        Node* temp = adjList[i];
        while (temp != NULL) {
            printf("-> %d ", temp->vertex);
            temp = temp->next;
        }
        printf("\n");
    }
}

// ---------- Main Driver ----------
int main() {
    int vertices, edges, src, dest, choice, startVertex;

    printf("Enter number of vertices: ");
    scanf("%d", &vertices);
    initGraph(vertices);

    printf("Enter number of edges: ");
    scanf("%d", &edges);

    printf("Enter edges (format: src dest), vertices numbered 0 to %d:\n", vertices - 1);
    for (int i = 0; i < edges; i++) {
        scanf("%d %d", &src, &dest);
        addEdge(src, dest);
    }

    do {
        printf("\n----- Graph Traversal Menu -----\n");
        printf("1. Display Adjacency List\n");
        printf("2. BFS Traversal\n");
        printf("3. DFS Traversal\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                displayGraph();
                break;
            case 2:
                printf("Enter starting vertex for BFS: ");
                scanf("%d", &startVertex);
                BFS(startVertex);
                break;
            case 3:
                printf("Enter starting vertex for DFS: ");
                scanf("%d", &startVertex);
                DFS(startVertex);
                break;
            case 4:
                printf("Exiting...\n");
                break;
            default:
                printf("Invalid choice! Try again.\n");
        }
    } while (choice != 4);

    return 0;
}

/*
 * Sample Input:
 * Vertices: 6
 * Edges: 7
 * Edge list: 0 1, 0 2, 1 3, 1 4, 2 4, 3 5, 4 5
 *
 * Sample Output (BFS from 0): 0 2 1 4 3 5
 * Sample Output (DFS from 0): 0 2 4 5 3 1
 * (Order depends on edge-insertion sequence in the adjacency list.)
 */
