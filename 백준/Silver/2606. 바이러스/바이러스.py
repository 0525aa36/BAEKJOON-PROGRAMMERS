# from collections import deque
import sys

# n = int(sys.stdin.readline())
# v = int(sys.stdin.readline())

# graph = [[] for i in range(n+1)]
# visited = [0] * (n+1)

# for i in range(v):
#     a,b = map(int,sys.stdin.readline().split())
#     graph[a] += [b]
#     graph[b] += [a]

# visited[1] = 1
# Q = deque([1])
# while Q:
#     c = Q.popleft()
#     for i in graph[c]:
#         if visited[i] == 0:
#             Q.append(i)
#             visited[i]=1
# print(sum(visited)-1)
###
n=int(sys.stdin.readline()) # 컴퓨터 개수
v=int(sys.stdin.readline()) # 연결선 개수
graph = [[] for i in range(n+1)] # 그래프 초기화
visited=[0]*(n+1) # 방문한 컴퓨터인지 표시
for i in range(v): # 그래프 생성
    a,b=map(int,sys.stdin.readline().split())
    graph[a]+=[b] # a에 b 연결
    graph[b]+=[a] # b에 a 연결 -> 양방향
def dfs(v):
    visited[v]=1
    for nx in graph[v]:
        if visited[nx]==0:
            dfs(nx)
dfs(1)
print(sum(visited)-1)
