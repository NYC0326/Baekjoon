#include <iostream>
#include <string.h>
using namespace std;

int main(void){
    int n;
    cin >> n;
    for (int i = 0; i < n; i++){
        int m;
        cin >> m;
        int price[110] = {0,};
        char name[30] = "";
        char max_name[30] = "";
        int max = 0;
        for (int j = 0; j < m; j++){
            cin >> price[j] >> name;
            if(j==0)
                strcpy(max_name, name);
            if(price[max]<price[j]){
                max = j;
                strcpy(max_name, name);
            }
        }
        cout << max_name << endl;
    }
}