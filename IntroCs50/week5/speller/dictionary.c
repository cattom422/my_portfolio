// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include<strings.h>
#include<stdlib.h>
#include<stdio.h>
#include <string.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;//

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

int count=0;
// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL; // All buckets initially empty
    }
    node *p=table[hash(word)];
    if (p == NULL )
    {
        return false;
    }
    while (strcasecmp(word,p->word)!=0)
    {
        p=p->next;
    }
    if (p == NULL)
    {
        return false;
    }
    return true;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    //Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL; // All buckets initially empty
    }
    FILE *source =fopen(dictionary,"r");
    if (source == NULL)
    {
        return false;
    }
    //node *table[N];
    //需要一个链尾吗?需要！！！！
    char wordlist[LENGTH + 1];
    while ( fscanf(source,"%s",wordlist) != EOF ) //end of file
    {
        //insert!
        node *new_word=malloc(sizeof(node));
        if (new_word == NULL)
        {
            return false;
        }
        strcpy(new_word->word, wordlist);
        new_word->next=table[hash(new_word->word)];
        table[hash(new_word->word)]=new_word;
        count+=1;

    }
    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int n=0;n<N;n++)
    {
        node *p=table[n];
        node *tmp;
        while (p!=NULL)
        {
            tmp=p->next;
            free(p);
            p=tmp;
        }
    }

    return true;
}
