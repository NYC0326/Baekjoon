#include <stdio.h>

int main(void){
    int n, m, a, b, sum=0, tmp, arr[100001]={0, };
    scanf("%d %d", &n, &m);
    for (int i = 1; i <= n; i++){
        scanf("%d", &tmp);
        sum += tmp;
        arr[i] = sum;
    }
    for (int i = 0; i < m; i++){
        scanf("%d %d", &a, &b);
        printf("%d\n", arr[b] - arr[a-1]);
    }
}