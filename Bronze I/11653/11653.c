#include <stdio.h>

int main(void){
    int n;
    scanf("%d", &n);
    while(n>1){
        int chk = 0;
        for(int i=2; 2*i<=n; i++){
            if(n%i==0){
                printf("%d\n", i);
                n /= i;
                chk = 1;
                break;
            }
        }
        if(chk==0){
            printf("%d", n);
            break;
        }
    }
}