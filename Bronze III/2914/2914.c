#include <stdio.h>

int main(void){
	int n, m;
	scanf("%d %d", &n, &m);
	if(n==1)
		printf("%d", n * m);
	else
		printf("%d", n * (m - 1) + 1);
}