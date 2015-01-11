#include "stdio.h"

int main(void)
{
	void swap(int *p1, int *p2);
	int a, b;
	int *pointer1, *pointer2;
	scanf("%d,%d",&a,&b);
	pointer1 = &a;
	pointer2 = &b;
	if(a<b)
	{
		swap(pointer1, pointer2);
	}
	printf("\n%d,%d\n",a, b);
}

void swap(int *p1, int *p2)
{
	int temp;
	temp = *p1;
	*p1 = *p2;
	*p2 = temp;
}
