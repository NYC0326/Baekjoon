import sys
from collections import deque
input = sys.stdin.readline

stk=deque()
n=int(input())
for i in range(n):
    a= input().split()
    if len(a)==2:   
        stk.append(int(a[1]))
    else:
        if a[0]=='2':
            if len(stk)==0:
                print(-1)
            else:
                p = stk.pop()
                print(p)
        
        if a[0]=='3':
            print(len(stk))
        
        if a[0]=='4':
            if len(stk)==0:
                print(1)
            else:
                print(0)
        
        if a[0]=='5':
            if len(stk)==0:
                print(-1)
            else:
                print(stk[-1])