"""
백준 1960 : 프린터 큐
"""

from collections import deque

for i in range(int(input())):

    N,M=map(int,input().split())

    deq=deque(list(map(int,input().split())))

    for j in range(len(deq)):
        deq[j]=(deq[j] , j)


    dp=[0]*N # 지워주는 횟수를 저장한다.
    count=0
    while deq:
        if deq[0][0]== max(deq)[0]:
            dp[deq[0][1]]=count # count는 삭제했을떄의 횟수
            deq.popleft()
            count+=1
        else:
            deq.append(deq.popleft())

    print(dp[M]+1)