#include <stdio.h>

int main(void){
    int n, tmp, ans=0, sum=0, val[1001]={0, };
    scanf("%d", &n);
    for (int i = 0; i < n; i++){
        scanf("%d", &tmp);
        val[tmp]++;
    }
    for (int i = 1; i < 1001; i++){
        if(val[i]!=0){
            while(val[i]!=0){
                sum += i;
                ans += sum;
                val[i]--;
            }
        }
    }
    printf("%d", ans);
}