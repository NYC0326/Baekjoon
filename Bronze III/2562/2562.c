#include <stdio.h>

int main(){
	int a, max=0, max_idx=0;
	for(int i=0; i<9; i++){
		scanf("%d", &a);
		if(max<a){
			max = a;
			max_idx = i+1;
		}
	}
	printf("%d\n%d", max, max_idx);
}