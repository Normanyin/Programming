#include "stdio.h"

int main(void)
{
	int max(int, int);
	int (*p)(int, int);
	int a,b,c;
	p = max;
	scanf("%d,%d",&a,&b);
	c = p(a,b);
	printf("a=%d,b=%d,max=%d\n",a,b,c);
}

int max(int a,int b)
{
	if(a>b)
	{
		return a;
	}
	else
	{
		return b;
	}
}
