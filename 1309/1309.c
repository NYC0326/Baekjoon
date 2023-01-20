#include <stdio.h>

int dp[100001] = {1,3};

int main(){
	int n;
	scanf("%d", &n);
	for (int i = 2; i <= n; i++)
		dp[i] = (dp[i - 1] * 2 + dp[i - 2])%9901;
	printf("%d", dp[n]);
}