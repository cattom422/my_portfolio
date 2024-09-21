#include<stdio.h>
#include<string.h>
int main(int argc,char *argv[])//input captitalized
{
    char *keey=argv[1];
    char *mian=argv[2];
    for (int i=0,n=strlen(mian);i<n;i++)
    {
        int p=mian[i]-65;
        printf("%c",keey[p]);
    }
    printf("\n");
}
