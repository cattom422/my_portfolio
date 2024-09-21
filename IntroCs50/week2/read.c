//index = 0.0588 * L - 0.296 * S - 15.8
#include<stdio.h>
#include<cs50.h>
#include<string.h>
char sign[3][2]={{' ','.'},{',',':'},{'.','?'}};//word,sen
double average(string sen,int si);
int main(void)
{
    //input
    string re=get_string("type: ");
    //f(x) length of sentences
    double index=5.88 * average(re,0) - 29.6 /(average(re,1)/average(re,0)+1)- 15.8;
    //output
    printf("%f\n",index);
}
double average(string sen,int si)//利用标志求平均
{
    int n=0;
    int sum=0;
    int former=0;
    for (int i=0, len1=strlen(sen);i<len1;i++)
    {
        for (int j=0;j<3;j++)
        {
            if (sen[i]==sign[j][si])
            {
                n++;
                sum+=(i-former);
                former=i+1;
            }
        }

    }
    return (double)sum/(double)n;
}
