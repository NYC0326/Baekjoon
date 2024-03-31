#include <stdio.h>

int main(void){
    int n, m, max = 0, tmp = 0, arr[100001] = {0, };
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    for (int i = 0; i < m; i++)
        max += arr[i];
    tmp = max;
    for (int i = m; i < n; i++){
        tmp += arr[i] - arr[i - m];
        if(tmp>max)
            max = tmp;
    }
    printf("%d", max);
}