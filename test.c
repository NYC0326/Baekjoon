#include <stdio.h>

int main(){
<<<<<<< HEAD
	printf("Hello World!");
	return 0;
=======
	int n;
	scanf("%d", &n);
	for(int i=0; i<n; i++){
		for(int j=0; j<n-i-1; j++)
			printf(" ");
		for(int j=0; j<2*i+1; j++)
			printf("*");
		printf("\n");
	}
	for(int i=n-1; i>0; i--){
		for(int j=i; j<n; j++)
			printf(" ");
		for(int j=0; j<2*i-1; j++)
			printf("*");
		printf("\n");
	}
>>>>>>> 5656c0ef17d1be28a3b70749bd0deac5770f1827
}