#include<stdio.h>
#include<cs50.h>
#include<string.h>
int scores[]={1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10};
int calscore(string p);
int main(void)
{
    /*input*/
    string p1,p2;
    int s1,s2;
    p1=get_string("player1: ");
    p2=get_string("player2: ");
    //f(x)
    s1=calscore(p1);
    s2=calscore(p2);
    if (s1>s2)
    {
        printf("1 wins!");
    }
    else if (s1==s2)
    {
        printf("tie!\n");
    }
    else
    {
        printf("2 wins!");
    }
}
int calscore(string p)//for(int i=0,len=strlen(p);i<len;i++) seems better!
{
    int i=0;
    int score=0;
    while (i<strlen(p))
    {
        if (p[i]<97)
        {
            score+=scores[p[i]-65];
        }
        else
        {
            score+=scores[p[i]-97];
        }

        i++;
    }
    return score;
}
