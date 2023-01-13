"""
백준 10866 : 덱
"""

from collections import deque
import sys
input=sys.stdin.readline

N=int(input())
deq=deque()

for i in range(N):

    L=list(input().split())

    if L[0]=="push_front":
        deq.appendleft(L[1])

    elif L[0]=="push_back":
        deq.append(L[1])

    elif L[0]=="pop_front":
        if deq:
            print(deq.popleft())
        else:
            print(-1)

    elif L[0]=="pop_back":
        if deq:
            print(deq.pop())
        else:
            print(-1)

    elif L[0]=="size":
        print(len(deq))

    elif L[0]=="empty":
        if deq:
            print(0)
        else:
            print(1)

    elif L[0]=="front":
        if deq:
            print(deq[0])
        else:
            print(-1)

    elif L[0]=="back":
        if deq:
            print(deq[-1])
        else:
            print(-1)