#include <stdio.h>
#include <stdlib.h>

#define MAX 100

void createGraph(int n, int graph[MAX][MAX]);
int checkEdge(int graph[MAX][MAX], int n, int u, int v);
int countEdges(int graph[MAX][MAX], int n);

int main() {
    int n, m;
    int u, v;
    int check;
    int graph[MAX][MAX];

    printf("Insert number of nodes n: ");
    scanf("%d", &n);

    createGraph(n, graph);

    printf("Insert node u: ");
    scanf("%d", &u);
    printf("Insert node v: ");
    scanf("%d", &v);

    check = checkEdge(graph, n, u, v);
    if (check) {
        printf("Edge exists between %d and %d\n", u, v);
    } else {
        printf("No edge exists between %d and %d\n", u, v);
    }

    printf("Total number of edges: %d\n", countEdges(graph, n));

    return 0;
}

void createGraph(int n, int graph[MAX][MAX]) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("Insert edge at position %d %d (1 yes, 0 no): ", i, j);
            scanf("%d", &graph[i][j]);
        }
    }
}

int checkEdge(int graph[MAX][MAX], int n, int u, int v) {
    if (graph[u][v] == 1)
        return 1;
    else
        return 0;
}

int countEdges(int graph[MAX][MAX], int n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (graph[i][j] == 1)
                count++;
        }
    }
    // For undirected graphs, divide by 2 to avoid double counting
    return count / 2;
}

