#include <stdio.h>
#include <math.h>

int main(void){
    int n, k, sum=0, cnt=0, tmp=0, max=0, min=8002, mode = 0, maxIndex= 0, arr[8001]={0, };
    scanf("%d", &n);
    for(int i=0; i<n; i++){
        scanf("%d", &k);
        arr[k + 4000]++;
        sum += k;
    }
    printf("%d\n", round(sum / n));
    for(int i=0; i<8001; i++){
        if(arr[i]!=0){
            cnt += arr[i];
        }
        if(cnt>=n/2+1){
            printf("%d\n", i-4000);
            cnt = 0;
            break;
        }
    }

    for (int i = 0; i < 8001; i++){
        if(mode<arr[i]){
            mode = arr[i];
            maxIndex = i;
        }
    }

    for (int i = 0; i < 8001; i++){
        if(arr[i]==mode)
            cnt++;
    }
    if(cnt==1)
        printf("%d\n", maxIndex - 4000);
    else{
        for(int i=0; i<8001; i++){
            if(arr[i]==mode)
                tmp++;
            if(tmp==2){
                printf("%d\n", i - 4000);
                break;
            }
        }
    }

    for (int i = 0; i < 8001; i++){
        if(arr[i]!=0){
            if(max<i)
                max = i;
            if(min>i)
                min = i;
        }
    }
    printf("%d", max-min);
}