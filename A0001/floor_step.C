/*

下楼问题。从楼上走到楼下共有h个台阶，每一步有三种走法：
走1个台阶，走2个台阶，走3个台阶。问有多少可走的方案。用递归思想和迭代思想编程。

*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

static int stack[1024];       // 存放每一步的台阶数
static int steps = 0;         // 走过的步数
static int num_of_method = 0; // 多少种走法
//递归详细版本，列出每一种走法的步骤
void NextStairs(int n)
{
	if(n == 0)
	{
		/* 走完所有台阶，打印本次的走法，即曾经走过的步骤 */
		printf("第%3d种走法[需%3d步] : ", ++num_of_method, steps);
		int i;
		for(i=0; i<steps; i++)
			printf("%d ", stack[i]);
		printf("\n");

		return;
	}

	if(n >= 1)
	{
		stack[steps++] = 1; // 本次走1个台阶
		NextStairs(n-1);
		steps --; 
	}
	if(n >= 2)
	{
		stack[steps++] = 2; // 本次走2个台阶
		NextStairs(n-2);
		steps --;
	}
	if(n >= 3)
	{
		stack[steps++] = 3; // 本次走3个台阶
		NextStairs(n-3);
		steps --;
	}
}
//迭代法
//此处是归纳出下一次z的迭代规律，下一次的z的值是上一次x,y,z的和，然后每次都要更新x,y,z
int fib3(int n)
{

       int x = 0, y = 0,z=1;
       int w, k;

       for (int j = 0; j < n; j++)
       {

           w = z;
           k = y;
           z = x + y + z;
           y = w;
           x = k;
           
           
       }

       return z;

}
//递归法
int dfib1(int n)
{
    if (n < 1)
    { return 0; }

    if (n == 1)
        return 1;
    if (n == 2)
        return 2;
    if (n == 3)
        return 4;
    return dfib1(n - 1) + dfib1(n - 2) + dfib1(n-3);
}

int main()
{
	int n;
	printf("enter a positive number: n=");
	scanf("%d", &n);

	//NextStairs(n);
	//printf("%d\n", dfib1(n));
	printf("%d\n", fib3(n));

	return 0;
}




