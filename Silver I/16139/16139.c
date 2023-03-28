#include <stdio.h>
#include <string.h>

int main(void){
    char arr[200001];
    scanf("%s", arr);
    int a[27][strlen(arr)], n;
    for (int i = 0; i < strlen(arr); i++){
        for (int j = 0; j<27; j++)
            a[j][i] = 0;
        a[arr[i] - 97][i]++;
    }
    for (int i = 1; i < strlen(arr); i++){
        for (int j = 0; j < 26; j++)
            a[j][i] += a[j][i - 1];
    }

    scanf("%d", &n);
    for (int i = 0; i < n; i++){
        char ch = 0;
        int x, y;
        scanf(" %c %d %d", &ch, &x, &y);
        if(x==0)
            printf("%d\n", a[ch - 97][y]);
        else
            printf("%d\n", a[ch - 97][y] - a[ch - 97][x - 1]);
    }
}