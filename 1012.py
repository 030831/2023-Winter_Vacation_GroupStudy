"""
백준 1012 : 유기농 배추
"""

"""
BFS - Breath first Search

한번 방문한 지점은 절대로 다시 방문하지 않는다.

"""
from collections import deque
import sys
input=sys.stdin.readline
dx=[-1,1,0,0]
dy=[0,0,-1,1]

# ( -1, 0) ( 1,0) ( 0,-1) (0,1)

def BFS(graph,visit , x, y):

    deq=deque()
    deq.append([x,y])
    visit[x][y]=True

    while deq:

        x,y=deq.popleft()

        for i in range(4):
            nx=x+dx[i] ; ny=y+dy[i]

            if 0<=nx<N and 0<=ny<M and not visit[nx][ny] and graph[nx][ny]==1: # 그래프 안에 있고 방문하지 않은 지점이라면.
                visit[nx][ny]=True #한번만 방문한다.
                deq.append([nx,ny])





for i in range(int(input())):
    M,N,K=map(int,input().split()) # 가로 , 세로 , 배추개수


    graph=[ [0]*M for _ in range(N) ]

    visit=[ [False]*M for _ in range(N) ]

    for j in range(K):
        a,b=map(int,input().split())
        graph[b][a]=1


    count=0


    for j in range(N):
        for k in range(M):
            if visit[j][k]==False and graph[j][k]==1: #방문하지 않았고 배추가 있는 지역이라면
                BFS(graph , visit , j , k)

                count+=1

    print(count)