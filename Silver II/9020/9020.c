#include <stdio.h>

int main(void){
	int n, k;
	int arr[10001] = {0, };
	arr[1] = 1;
    
    for(int i=2; i<=10000/2; i++){
        for(int j=2; i*j<=10000; j++){
            arr[i*j] = 1;
        }
    }
    
    scanf("%d", &n);
    
	for(int i=0; i<n; i++){
		scanf("%d", &k);
		for(int j=k/2; j>0; j--){
			if(arr[j]==0 && arr[k-j]==0){
                printf("%d %d\n", j, k - j);
                break;
            }
		}
	}
}