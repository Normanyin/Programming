#include "stdio.h"

int main(void)
{
	int a[10];
	int b[10];
	int i,t;
	for (i = 0; i < 10; i++)
	{
		a[i] = 0;
		scanf("%d", &b[i]);
	}
	for (i = 0; i < 10; i++)
	{
		t = b[i];
		a[t]++;
	}
	printf("after bucket sort:\n");
	for (i = 0; i < 10; i++)
	{
		for (t = 0; t < a[i]; t++)
			printf("%d ", i);
	}
	
	return 0;
}
