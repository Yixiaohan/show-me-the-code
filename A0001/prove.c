#include<stdio.h>
//递归和归纳都是将复杂问题简单化的方法，只是方向不同，递归是"从一般到个别"，归纳是"从个别到一般"

//用递归的思想来证明数学归纳法
void prove1(int n)
{
	if(n == 0){
		printf("step 0,the P(%d) true.\n", n);
	}else{
		prove1(n-1);
		printf("step %d,if P(%d) true ,then P(%d) true also.\n", n, n - 1, n);
    	printf("so,we can say \"P(%d) true.\"\n", n);

	}
}

//用循环来表示数学归纳法
void prove2(int n)
{
    int k;

    printf("now we'll prove P(%d) true.\n", n);
    k = 0;
    printf("step 0 can prove P(%d) true.\n", k);
    while(k < n)
    {
        printf("step %d can say \" if P(%d) true,then P(%d) true also\".\n", k + 1, k, k + 1);
        k = k + 1;
    }
    printf("All prove over.\n");
}

int main()
{
    int n;
    printf("input your number:n=");
    scanf("%d",&n);
    printf("\n");
    prove1(n);
    printf("\n");
    prove2(n);
    return 0;
}
