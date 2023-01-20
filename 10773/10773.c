#include <stdio.h>
#include <stdlib.h>

#define MAX_STACK_SIZE 100001

typedef int element;
element stack[MAX_STACK_SIZE];
int top = -1;

int is_empty(){
	if (top == -1)
		return 1;
	else return 0;
}

int is_full(){
	return (top==(MAX_STACK_SIZE-1));
}

void push(element item){
	stack[++top] = item;
}

element pop(){
	if(is_empty())
		return -1;
	else{
		int n = stack[top];
		stack[top--] = 0;
		return n;
	}
}

int main(void){
	int stackSize, m, sum = 0;
	scanf("%d", &stackSize);
	for (int i = 0; i < stackSize; i++){
		scanf("%d", &m);
		if(m==0)
			sum -= pop();
		else{
			push(m);
			sum += m;
		}
	}
	printf("%d", sum);
}