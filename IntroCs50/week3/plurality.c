#include<stdio.h>
#include<string.h>

int main(int argc,char *argv[])
{
    //input
    int vo_num[argc-1];
    for (int l=0;l<(argc-1);l++)
    {
        vo_num[l]=0;
    }
    //1st number of voters
    int num_voters;
    printf("number of voters: ");
    scanf("%i",&num_voters);
    //2nd votes(invalid to do)
    char cur[100];
    for (int i=0;i<num_voters;i++)
    {
        strcpy(cur," ");
        printf("plz vote: ");
        scanf("%s",cur);
        int j=0;
        do
        {
            j++;
        }
        while(strcmp(argv[j],cur)!=0);
        vo_num[j-1]+=1;
    }
    //output
    for (int l=0;l<(argc-1);l++)
    {
        printf("%i\n",vo_num[l]);
    }
}
