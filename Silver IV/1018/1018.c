#include <stdio.h>
#define min(a,b) a<b?a:b

int main(){
	char arr[50][50];
	int n, m, ans=32, cnt, cnt2;
	scanf("%d %d", &n, &m);
	for(int i=0; i<n; i++)
		scanf("%s", &arr[i]);
	for(int i=0; i<n-7; i++){
		for(int j=0; j<m-7; j++){
			cnt=0, cnt2=0;
			for(int a=i; a<i+8; a++){
				for(int b=j; b<j+8; b++){
					if((a+b)%2==0){
						if(arr[a][b]=='B')
							cnt2++;
						else
							cnt++;
					}
					else{
						if(arr[a][b]=='B')
							cnt++;
						else
							cnt2++;
					}
				}
			}
			ans = min(ans, cnt);
			ans = min(ans, cnt2);
		}
	}
    printf("%d %d\n", cnt, cnt2);
    printf("%d", ans);
}