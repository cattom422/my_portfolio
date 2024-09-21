//greedy cashier
#include<stdio.h>

int main(void)
{
	//input
	int owe;
	int times=0;
	int k=25,n=10,m=5,z=1;
	printf("? ");
    scanf("%d",&owe);
	//f(x)
	while (owe>0)
	{
		times++;
		if (owe>=k)
		{
			owe-=k;
		}
		else if (owe>=n)
		{
			owe-=n;
		}
		else if (owe>=m)
		{
			owe-=m;
		}else if (owe>=z)
		{
			owe-=z;
		}
	}
	printf("%d\n",times);
}
void
