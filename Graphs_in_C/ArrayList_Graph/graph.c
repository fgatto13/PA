// graph.c
#include <stdio.h>
#include <stdlib.h>
#include "graph.h"
#include "list.h"

graph createGraph(int n) {
    graph G = (graph)malloc(n * sizeof(list));
    if (G == NULL) {
        printf("Memory allocation failed\n");
        exit(1);  // Exit if memory allocation fails
    }

    for (int i = 0; i < n; i++) {
        G[i] = newList();  // Initialize each list head to NULL (or use newList() for clarity)
    }
    return G;
}

int checkEdge(int u, int v, graph G) {
    list current = G[u];
    while (current != NULL) {
        if (getFirst(current) == v) {
            return 1;  // Edge found
        }
        current = tailList(current);
    }
    return 0;  // Edge not found
}

int countEdges(graph G, int n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        list current = G[i];
        while (current != NULL) {
            count++;
            current = tailList(current);
        }
    }
    return count;
}
