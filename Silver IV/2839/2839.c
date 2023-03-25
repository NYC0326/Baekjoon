#include <stdio.h>

int main(void){
    int n, dp[5001], tmp;
    for (int i = 0; i < 5001; i++)
        dp[i] = -1;
    dp[3] = 1;
    dp[5] = 1;
    scanf("%d", &n);
    for(int i=6; i<=n; i++){
        if(dp[i-3]!=-1&&dp[i-5]!=-1){
            if(dp[i-3]<dp[i-5])
                dp[i] = dp[i - 3] + 1;
            else
                dp[i] = dp[i - 5] + 1;
        }
        else if(dp[i-3]!=-1)
            dp[i] = dp[i - 3] + 1;
        else if(dp[i-5]!=-1)
            dp[i] = dp[i - 5] + 1;
    }
    printf("%d", dp[n]);

    for (int i = 0; i < 20; i++)
        printf("%d ", dp[i]);
}