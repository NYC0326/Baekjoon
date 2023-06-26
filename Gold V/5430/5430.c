#include <stdio.h>
#include <stdlib.h>
#define swap(a, b) {int t = a; a = b; b = t;}

int	t, q[100001], n, first, last;
char	p[100001], nums[400001];

int	D()
{
	if (first == last) {
		printf("error\n");
		return (1);
	}
	if (last < first)
		first--;
	else
		first++;
	return (0);
}

void R(){
	swap(last, first);
}

void print() {
    int i, j;

    if (first==last) {
		printf("[]\n");
		return ;
	}
	printf("[");
	i = first;
	j = last;
	if (i > j){
		i--;
		for(; i > j; i--)
			printf("%d,", q[i]);
	}
	else{
		for(; i < j - 1; i++)
			printf("%d,", q[i]);
	}
	printf("%d]\n", q[i]);
}

void push(int num){
	q[last++] = num;
}

int	main(void){
	int	err_flag;

	scanf("%d", &t);
	for(int i = 0; i < t; i++)	{
		first = 0;
		last = 0;
		err_flag = 0;
		scanf("%s %d %s", p, &n, nums);
		for(int j = 1; nums[j]; j++){
			if ('0' <= nums[j] && nums[j] <= '9')	{
				push(atoi(&nums[j]));
				while ('0' <= nums[j] && nums[j] <= '9')
					j++;
			}
		}
		for (int j = 0; p[j]; j++){
			if (p[j] == 'D'){
				if (D()){
					err_flag = 1;
					break ;
				}
			}
			else
				R();
		}
		if (!err_flag)
			print();
	}
}