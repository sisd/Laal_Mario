#include<stdio.h>
int z=0;
int recc(int n)
{
	if(n<=0)return 0;
	recc(n-1);
	recc(n/2);
	int i;
	for(i=0;i<n;i++)
	z++;
	return 0;
}
int main()
{
int n;
scanf("%d",&n);
recc(n);
printf("%d\n",z);
return 0;
}
