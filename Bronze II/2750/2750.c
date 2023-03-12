#include <stdio.h>

int main(void){
    int a, n, cnt=0, arr[2002] = {0, };
    scanf("%d", &n);
    for(int i=0; i<n; i++){
        scanf("%d", &a);
        arr[a+1000]++;
    }
    for(int i=0; i<2002; i++){
        if(arr[i]!=0){
            printf("%d\n", i-1000);
            cnt++;
        }
        if(cnt==n)
            break;
    }
}