#ifndef GRAPH_H
#define GRAPH_H

#include "list.h"

typedef list* graph;

graph createGraph(int n);
int checkEdge(int u, int v, graph G);
int countEdges(graph G);

#endif // GRAPH_H
