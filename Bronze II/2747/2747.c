#include <stdio.h>

int main(void){
    int a = 1, b = 1, tmp, n;
    scanf("%d", &n);
    for (int i = 0; i < n - 2; i++){
        tmp = a + b;
        a = b;
        b = tmp;
    }
    printf("%d", b);
}