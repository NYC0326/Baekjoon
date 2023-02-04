#include <stdio.h>

int main(void){
	int a, b, c, sec;
	scanf("%d %d %d\n%d", &a, &b, &c, &sec);
	while(sec+c>=60){
		b++;
		sec -= 60;
	}
	while(b>=60){
		a++;
		b -= 60;
	}
	printf("%d %d %d", a % 24, b, c+sec);
}