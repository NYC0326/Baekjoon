#include <stdio.h>

int main(void){
    int n, k, scores[10001] = {0 ,}, score, cnt=0;
    scanf("%d %d", &n, &k);
    for(int i=0; i<n; i++){
        scanf("%d", &score);
        scores[score]++;
    }
    for(int i=10000; i>=0; i--){
        if(scores[i]!=0)
            cnt += scores[i];
        if(cnt>=k){
            printf("%d", i);
            break;
        }
    }
}