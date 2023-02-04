#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char n[100001];

int compare(const void* a, const void* b) {
	const char* n1 = (const char*)a;
	const char* n2 = (const char*)b;
	if (*n1 > *n2) {
		return -1;
	}
	else if (*n1 == *n2) {
		return 0;
	}
	else {
		return 1;
	}
}

int main(){
	int i = 0, sum = 0;
	scanf("%s", &n);
	if(strchr(n, '0') == NULL || n[0] == '0'){
		printf("-1");
		return 0;
	}
	while(n[i] != '\0'){
		sum += n[i] - 48;
		i++;
	}
	if(sum%3!=0 || sum==0){
		printf("-1");
		return 0;
	}
	else
		qsort(n, sizeof(n) - 1, sizeof(char), compare);
	printf("%s", n);
	return 0;
}