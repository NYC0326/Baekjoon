#include <stdio.h>

int arr[1000001] = {0, };

int main(void){
	int a, b;
	arr[1] = 1;
    
    scanf("%d %d", &a, &b);
    
    for(int i=2; i<=b/2; i++){
        for(int j=2; i*j<=b; j++){
            arr[i*j] = 1;
        }
    }
    
    for(int i=a; i<=b; i++){
        if(arr[i] == 0)
            printf("%d\n",i);
    }
    
    return 0;
}