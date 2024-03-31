#include <stdio.h>

int main(void){
    int num[11]={0,}, k, sum=0, cnt=0;
    for(int i=0; i<5; i++){
        scanf("%d", &k);
        num[k / 10] += 1;
        sum += k;
    }
    printf("%d\n", sum / 5);

    for(int i=1; i<10; i++){
        if(num[i]!=0)
            cnt += num[i];
        if(cnt>=3){
            printf("%d", i * 10);
            break;
        }
    }
}