#ifndef LIST_H
#define LIST_H

typedef struct node {
    int v;
    struct node* next;
} node;

typedef node* list;

list newList(void);
int emptyList(list l);
list tailList(list l);
list consList(int v, list l);
int getFirst(list l);

#endif // LIST_H
