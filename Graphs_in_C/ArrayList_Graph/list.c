#include <stdio.h>
#include <stdlib.h>
#include "list.h"

struct node
{
    int v;
    struct node* next;
};

list newList(void)
{
    return NULL;
}

int emptyList(list l)
{
    return l == NULL;
}


list consList(int v, list l)
{
    struct node *newNode;
    newNode = malloc (sizeof(struct node));
    if (newNode != NULL) {
     	newNode->v = v;
      	newNode->next = l;
	    l = newNode; 
	}
    return l;
}

list tailList(list l)
{
    list temp;
    if (l != NULL)    
	    temp = l->next;
    else 
        temp = NULL;
    return temp;
}

int getFirst (list l)
{
    int e;
    if(l != NULL)    
	    e = l->v;
    else 
        e = 0;
    return e;
}