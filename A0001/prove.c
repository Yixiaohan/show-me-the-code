#include<stdio.h>

void prove(int n)
{
	if(n == 0){
		printf("step 1,the P(%d) true.\n",n);
	}else{
		prove(n-1);
		printf("step 2,if P(%d) trye ,then P(%d) true also.\n", n-1,n);
    	printf("so,we can see \"P(%d) true.\"\n",n);

	}
}

int main()
{
    int n;
    printf("input your number:n=");
    scanf("%d",&n);
    prove(n);
    return 0;
}
