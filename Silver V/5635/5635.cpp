#include <iostream>
using namespace std;

// 1. 조건문 엄청 나눠서 푸는 방법

int main(void){
	int n, min=0, max=0;
	cin >> n;
	char name[n][20];
	int birthday[n][3];

	for (int i = 0; i < n; i++){
		cin >> name[i] >> birthday[i][0] >> birthday[i][1] >> birthday[i][2];
		if(birthday[max][2]>birthday[i][2])
			max = i;
		else if (birthday[max][2] == birthday[i][2]){
			if (birthday[max][1] > birthday[i][1])
				max = i;
			else if(birthday[max][1] == birthday[i][1]){
				if (birthday[max][0] > birthday[i][0])
					max = i;
			}
		}

		if(birthday[min][2]<birthday[i][2])
			min = i;
		else if (birthday[min][2] == birthday[i][2]){
			if (birthday[min][1] < birthday[i][1])
				min = i;
			else if(birthday[min][1] == birthday[i][1]){
				if (birthday[min][0] < birthday[i][0])
					min = i;
			}
		}
	}
	cout << name[min] << endl << name[max] << endl;
}