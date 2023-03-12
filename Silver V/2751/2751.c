#include <stdio.h>

int num[2000002]={0,};

int main(void){
    int n, k;
    scanf("%d", &n);
    for(int i=0; i<n; i++){
        scanf("%d", &k);
        num[k+1000000]++;
    }
    for(int i=0; i<2000002; i++){
        if(num[i]==1)
            printf("%d\n", i-1000000);
    }
}