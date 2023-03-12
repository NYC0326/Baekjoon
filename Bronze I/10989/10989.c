#include <stdio.h>

int main(){
	int n, a[10001]={0, }, tmp;
	scanf("%d", &n);
	for(int i=0; i<n; i++){
		scanf("%d", &tmp);
		a[tmp]++;
	}
	for(int i=1; i<10001; i++){
		if(a[i]!=0){
			for(int j=0; j<a[i]; j++)
				printf("%d\n", i);
		}
	}
}