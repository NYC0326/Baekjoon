#include <stdio.h>

int main(void){
	int a, b, k;
	scanf("%d\n%d", &a, &b);
	k = b;
	while(b!=0){
		printf("%d\n", b % 10 * a);
		b /= 10;
	}
	printf("%d", a * k);
}