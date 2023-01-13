"""
백준 15828 : Router
"""

from collections import deque

N=int(input())

L=deque()

while True:

    if len(L)>N:
        L.pop()

    A=int(input())

    if A==-1:
        break

    if A==0:
        L.popleft()

    else:
        L.append(A)

if not L:
    print("empty")
else:
    print(*L)