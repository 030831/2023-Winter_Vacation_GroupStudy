"""
백준 11866 : 요세푸스 문제 0
"""

from collections import deque
N,K=map(int,input().split())

L=[ i for i in range(1,N+1) ]
L=deque(L)

L2=[]
for i in range(N):

    check=0
    while True:
        if check==K-1:
            break
        L.append(L.popleft())
        check+=1

    L2.append(L.popleft())


print("<" , end="")
for i in range(len(L2)-1):
    print("%d, "%L2[i] , end="")

print("%d>"%L2[-1])
