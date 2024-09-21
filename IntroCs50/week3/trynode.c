#include<stdio.h>
#include<stdlib.h>//正序输出
typedef struct node
{
    int number;
    struct node *next;
}node;
int main(int argc,char *argv[])
{
    node *head=NULL;
    node *n=malloc(sizeof(node));
    n->number=atoi(argv[1]);
    n->next=NULL;
    head=n;
    node *tail=n;
    for (int i=2;i<argc;i++)
    {
        node *m=malloc(sizeof(node));
        m->number=atoi(argv[i]);
        m->next=NULL;
        tail->next=m;
        tail=m;
    }
    node *ptr=head;
    while (ptr->next!=NULL)
    {
        printf("%i\n",ptr->number);
        ptr=ptr->next;
    }
    printf("%i\n",ptr->number);
}
