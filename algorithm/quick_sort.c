#include "stdio.h"

int a[10];

void quicksort(int left, int right)
{
	if (left > right)
		return;
	int base = a[left];
	int head = left;
	int end = right;
	while(right > left)
	{
		if(a[right] >= base)
		{
			right--;
		}
		else if(a[left] <= base)
		{
			left++;
		}
		else
		{
			int temp = a[left];
			a[left] = a[right];
			a[right] = temp;
		}
	}
	a[head] = a[left];
	a[left] = base;
	quicksort(head, left-1);
	quicksort(left+1, end);
}
int main (void)
{
	int i;

	for(i = 0; i < 10; i++)
	{
		scanf("%d", &a[i]);
	}
	quicksort(0,9);
	for(i = 0; i < 10; i ++)
	{
		printf("%d ", a[i]);
	}
	return 0;
}

