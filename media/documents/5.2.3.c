#include<stdio.h>
int main()
{
 int i,f,n;
 printf("Enter the limit:");
 scanf("%d", &n);
 for(i=1;i<=n;i++)
 {
  f= n*i;
  printf("%d * %d = %d\n",n,i,f);
  
 }
 
return 0;
}

