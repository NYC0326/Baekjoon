#include <stdio.h>

int main(void){
    int dp[41] = {0,}, n;
    dp[1] = 1, dp[2] = 1;
    scanf("%d", &n);
    for (int i = 3; i<=n; i++)
        dp[i] = dp[i - 1] + dp[i - 2];
    printf("%d %d", dp[n], n - 2);
}