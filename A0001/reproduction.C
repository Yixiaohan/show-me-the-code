/*************************************************************************
	> File Name: reproduction.c
	> Author: wangxiaoxian
	> Mail: 634897019@qq.com 
	> Created Time: Fri 03 Jun 2016 09:54:11 PM CST
 ************************************************************************/
//一只动物，出生2天后开始以每天1只的速度繁殖后代，假设第一天，有1只这样的动物，
//那么，n天后，一共多少只？

#include<stdio.h>

//找出递推式，用递归思想编程。
int reproduction(int n)
{
    if (n < 1)
        return 0;

    if (n == 1)
        return 1;
    if (n == 2)
        return 1;
    return reproduction(n-1) + reproduction(n-2);
}

//迭代思想
int reproduction_itera(int n)
{
    int x = 0, y = 1;    
    int w;
    for (int j = 0; j < n - 1; j++)
    {
        w = y;
        y = x + y;
        x = w;
    }
    return y;
}

int main()
{
    int days;
    printf("input how many days:days=");
    scanf("%d", &days);
    printf("the sum of reproductions:%d\n", reproduction(days));
    printf("the sum of reproductions:%d\n", reproduction_itera(days));
    return 0;
}
