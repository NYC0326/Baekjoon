#include <stdio.h>
#define MAX 1000000

int dp[MAX] = {0,};

int main(){
	for(int i=2; i<=MAX/2; i++){
        	for(int j=2; i*j<=MAX; j++){
            	dp[i*j] = 1;
        }
	}
	
	while(1){
		int n, t=0;
		scanf("%d", &n);
		if(n==0)
			break;
		for (int i = 3; i <= n / 2; i+=2){
			if(dp[i]==0 && dp[n-i]==0){
				printf("%d = %d + %d\n", n, i, n-i);
				t = 1;
				break;
			}
		}
		if(t==0)
			printf("Goldbach's conjecture is wrong.");
	}
}