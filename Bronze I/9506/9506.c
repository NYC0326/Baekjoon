#include <stdio.h>

int main(void){
    while(1){
        int a, p, sum=0, num[100001]={0,};
        scanf("%d", &a);
        if(a==-1)
            break;
        for(int i=1; i<a; i++){
            if(a%i==0){
                num[i] = 1;
                p = i;
            }
        }
        for(int i=1; i<a; i++){
            if(num[i]==1)
                sum += i;
        }
        if(sum==a){
            printf("%d = ", a);
            for(int i=1; i<p; i++){
                if(num[i] == 1)
                    printf("%d + ", i);
            }
            printf("%d\n", p);
        }
        else
            printf("%d is NOT perfect.\n", a);
    }
}