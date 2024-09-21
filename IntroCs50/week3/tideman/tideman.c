#include <cs50.h>
#include <stdio.h>
//大概算法：先比较再locked up
// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];//锁定

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
} pair;

// Array of candidates
string candidates[MAX];//input

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;

    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }

        for (int k=0;k<candidate_count;k++)
    {
        for (int m=0;m<candidate_count;m++)
        {
            if (k!=m)
            {
            preferences[k][m]=0;
            }
        }
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }//input 1st

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }//根据人数进行初始化
    pair pairs[candidate_count*(candidate_count-1)/2];
    pair_count = 0;//？
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)//对每个投票者进行分析
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}//done

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    // 输入 0123...?
    // ranks[i] is voter's ith preference
    for (int l=0;l<candidate_count;l++)
    {
        if (candidates[l]==name)
        {
            ranks[rank]=l;
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    // preferences[i][j] is number of voters who prefer i over j  int preferences[MAX][MAX];
    for (int k=0;k<candidate_count;k++)
    {
        for (int m=k+1;m<candidate_count;m++)
        {
            preferences[ranks[k]][ranks[m]]++;
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)//记录胜利幅度 deal with preferences
{

    int f=0;
    for (int k=0;k<candidate_count;k++)
    {
        for (int m=k+1;m<candidate_count;m++)
        {
            if (f<candidate_count*(candidate_count-1)/2)
            {
                if(preferences[ranks[k]][ranks[m]]>preferences[ranks[m]][ranks[k]])
                {
                    pairs[f].winner=k;
                    pairs[f].loser=m;
                    f++;
                }
            }
        }
    }

    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)//bubble sort
{
    pair tmp;
    for (int q=0;q<candidate_count*(candidate_count-1)/2-1;q++)
    {
        for (int b=candidate_count*(candidate_count-1)/2-2;b>q-1;b--)
        {
            if ((preferences[pairs[b].winner][pairs[b].loser] - preferences[pairs[b].loser][pairs[b].winner])< (preferences[pairs[b+1].winner][pairs[b+1].loser] - preferences[pairs[b+1].loser][pairs[b+1].winner]))
            {
                tmp=pairs[b];
                pairs[b]=pairs[b+1];
                pairs[b+1]=tmp;
            }
        }
    }
    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    
    return;
}

// Print the winner of the election
void print_winner(void)
{
    // TODO
    return;
}
