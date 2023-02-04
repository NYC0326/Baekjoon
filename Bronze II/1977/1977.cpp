#include <iostream>
using namespace std;

int main(void){
	int n, m;
	cin >> n >> m;
	int min=0, sum=0;
	for (int i = 1; i < 101; i++){
		if(i*i>=n && i*i<=m){
			if(min==0)
				min = i * i;
			sum += i * i;
		}
	}
	if(min==0){
		cout << -1 << endl;
		return 0;
	}
	cout << sum << endl;
	cout << min << endl;
}