#include <iostream>
using namespace std;

// 2. 단순 숫자로 합쳐서 비교하는 방법

int bday(int bday[]){
	return bday[2] * 10000 + bday[1] * 100 + bday[0];
}

int main(void){
	int n, min=0, max=0;
	cin >> n;
	char name[n][20];
	int birthday[n][3];

	for (int i = 0; i < n; i++){
		cin >> name[i] >> birthday[i][0] >> birthday[i][1] >> birthday[i][2];
		// 최고령자 구하기
		if(bday(birthday[max])>bday(birthday[i]))
			max = i;
		if(bday(birthday[min])<bday(birthday[i]))
			min = i;
	}
	
	cout << name[min] << endl << name[max] << endl;
}