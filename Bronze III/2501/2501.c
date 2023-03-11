#include <stdio.h>

int main(void){
	int a, b, num[10001] = {0 ,}, cnt=0, ans=0;
	scanf("%d %d", &a, &b);
	for(int i=1; i<=a; i++){
		if(a%i==0)
			cnt++;
		if(cnt==b){
			printf("%d", i);
			break;
		}
	}
	if(cnt<b)
		printf("0");
}