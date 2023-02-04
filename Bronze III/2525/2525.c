#include <stdio.h>

int main(void){
	int a, b, c, min;
	scanf("%d %d\n%d", &a, &b, &c);
	min = b + c;
	while(min>=60){
		a++;
		min -= 60;
	}
	printf("%d %d", a % 24, min);
}