"""
백준 2164 : 카드 2
"""

from collections import deque

N=int(input())

L=[ i for i in range(1,N+1) ]

L=deque(L)


while len(L)!=1:

    L.popleft()
    L.append(L.popleft())

print(L[0])